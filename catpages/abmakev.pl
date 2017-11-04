#!/usr/local/bin/perl

# abmakev.pl

# produce html pages or snippets from templates
# defaults to converting *.tmpl -> *.html in the current working directory
# will add optional params for FROM and TO directories
# generally run in an /includes directory to produce files for inclusion by PHP

# should: 
# accepts param -c[id] for category id to apply, 
# or find file named .catid or .catname in current dir
# otherwise parses from each template file as
#  [|CATID:nnn|]
# or [|CATNAME:xxx|] 


#use Smart::Comments;

use File::Find;
use Carp;
 
BEGIN {
      unshift (@INC, '.');
      unshift (@INC,"/w/abra/lib");
}

use AbHeader qw(:all);
use AbUtils;
use AbSecure;
use AbMacros;
use AbDomains;
#use Mysql;
use DBI;
use CommandWeb;
use AbCat;
use Abra;


$DEFAULT_CAT = 301;

# TODO: use module to do switches more nicely
$gen_all = 0;
if ($ARGV[0] eq '-a') {
	$gen_all = 1;
	shift @ARGV;
}

$gencat = $ARGV[0] || $DEFAULT_CAT;

$default_template_file = $ARGV[1] || '';

$userdef_target_file = $ARGV[2] || '';

print "Got target file $userdef_target_file...\n";
$rootdom = &AbDomains::globalGetDomainfromCat($gencat);

$abdomain = new AbDomains($rootdom);

$SHOW_FROM_LEVEL = $abdomain->getShowFromLevel;  # we are showing only under /root/UserDefined

$DEFAULT_FILE_NAME = 'abra.php';   # could be index.html, but then we don't overwrite ourselves...

$ALTERNATE_FILE_NAME = 'abra.php';  # if we don't want overwriting, make this different

$MOBILE_FILE_NAME = 'ab_mobile.php';  # for mobile phones

$DEFAULT_TEMPLATE_DIR = $abdomain->getTemplateDir;

$ROOTCAT = $abdomain->getRootCat;	# right now will match gencat
$ROOTLEVEL = $SHOW_FROM_LEVEL;		# currently they have to match, may not
					# TODO separate out

$AB_INDEX_FILE = '/home/sites/iwtucson/catpages/abindex.php';

$DEFAULT_TEMPLATE_FILE = "$ROOTCAT".'.tmpl';

$DEFAULT_MOBILE_TEMPLATE = "$ROOTCAT".'_mobile.tmpl';

if (! $default_template_file) {
	$default_template_file = $DEFAULT_TEMPLATE_FILE;
}

$ROOT_TARGET_DIR = $abdomain->getTargetDir;

print "ROOT TARGET DIR = ".$ROOT_TARGET_DIR."\n\n";

$MAX_ITEMS = 355;
$MAX_SHOW_IMGS = 3;
$NUM_SQUARE_IMGS = 4;
$MAX_SUBCATS = 96;
$MAX_RELCATS = 25;

$MAX_URL_DISPLAY_LENGTH = 40;	 # otherwise may mess up blog displays

$MAX_ITEM_LENGTH = 800;	# how much of short_content should we show on cat page

$MIN_FRONTPAGE_INTEREST = 20;  # only show good images on the front page

	$DBNAME = 'rcats';
	$DBUSER = 'rcats';
	$DBPASS = 'meoow';
	$THISCGI = "http://abra.btucson.com/cgi/ab.pl";
	$ADMINUSER = 1;
$debug = 0;

%HAVECATS =();


if ($ARGV[1]) { $explicit_template = 1; } else { $explicit_template = 0; }

$SHOWDELMASK = 1;
my %templatehash = ();


# Use MySQL (or DBI) to connect
$abra = new Abra;


if (!$dbh) {
	print "Error - cannot get database handle\n";
	exit;
}

$curdir = `pwd`;
chomp $curdir;
$curcat = 0;
$rootcat = 0;
$target_dir = '';
$template_file = '';
$mobile_template_file = $DEFAULT_TEMPLATE_DIR.'/'.$DEFAULT_MOBILE_TEMPLATE;  # only one

# check dir for .catid or .catname, set defaultcat
if ( -e "PARENT_CAT_ID" ) {
	open F,"PARENT_CAT_ID";
	$rootcat = <F>;
	close F;
}
chomp $rootcat;


print "Working on category $gencat using template $default_template_file\n";


if ( -e $default_template_file ) {
	$default_template_file = $curdir .'/'.$default_template_file;
} else {
	$default_template_file =  $DEFAULT_TEMPLATE_DIR.'/'.$default_template_file;
	if  ( ! -e $default_template_file ) {
		croak "No template file $default_template_file";
	}
}

$q = "select catcode from rcatdb_categories where id = $ROOTCAT";
($rootcatcode) = $dbh->selectrow_array($q);

$rootcatcode = $dbh->quote($rootcatcode);

if ($gencat && ! $gen_all) {
	$q = "select * from rcatdb_categories where security_level = 0 AND id = $gencat";
	print "Query is $q\n";
} else {

	#$q0 = "select cid from rcatdb_items where NOW() - ENTERED < 20000001000000";
	$q0 = "select distinct cid from rcatdb_items where NOW() - ENTERED < 80000001000000";
	$updatecats = $dbh->selectall_arrayref($q0);
	$updatestring = '';
	foreach my $upcatref (@$updatecats) {
		my ($upcat) = @$upcatref;
		$updatestring .= " id = $upcat ";
		$updatestring .= "or";
	}
	chop $updatestring; chop $updatestring;
	print $updatestring;

#	&prompt("Are you sure you want to regen ALL categories? ");
#	print("Doing everything new since yesterday = ".$#$updatecats." cats\n");
	$q = "select * from rcatdb_categories where security_level = 0  AND LEFT(catcode, $ROOTLEVEL) = LEFT($rootcatcode, $ROOTLEVEL) order by id ";
#	$q = "select * from rcatdb_categories where security_level = 0 and ($updatestring)";
}

$sth = $dbh->prepare($q);

$sth && $sth->execute() || die("Can't execute $q");

# TODO this should be done item by item so we don't miss those with
# optional types missing
@apply_types = ('ab_biz_org');

warn ("There are ".$sth->rows()." rows\n query was $q");

while ($ref = $sth->fetchrow_hashref('NAME_uc')) {

	my $curcat = $ref->{ID}; 
	my $template_file = $curdir . '/'.$curcat.'.tmpl'; # cat-specific template?
	if ($explicit_template || (! -e $template_file)) {
		# TODO: actually should backup by catcode...
		$template_file = $default_template_file; # we know this exists
	} else {
		print "Using $template_file for $curcat\n";
	}
	my $target_dir = $ROOT_TARGET_DIR . $ref->{'REL_URL'};


	$target_dir =~ s/\'//g;
	if (! -e $target_dir) {
		mkdir($target_dir,0755);
	}

#	if (! -e "$target_dir/abindex.php") {
		`cp -a $AB_INDEX_FILE '$target_dir'`;
#	}
	
	@apply_types = ();
$debug && print "We foudn types ",@apply_types,"\n";

	my $target_file = "$target_dir/$DEFAULT_FILE_NAME";

	my $mobile_target_file = "$target_dir/$MOBILE_FILE_NAME";

	if ( -e "$target_file") {
		$target_file = "$target_dir/$ALTERNATE_FILE_NAME";
	}
print "now target file is $target_file\n";
	# If the user passed an explicit target file use that
	if ($userdef_target_file) {
		$target_file = $userdef_target_file;
	}
print "Now target file is $target_file\n";

print "Processing cat # $curcat $ref->{'NAME'} , outputting to \n$target_file using template $template_file\n\n";

	$target_file =~ s/\'//g;

	&process_template_file($curcat, $template_file, $target_file);
		
	&process_template_file($curcat, $mobile_template_file, $mobile_target_file);

}
$sth->finish;
$dbh->disconnect;
1;

sub process_template_file {

	my $curcat = shift;
	my $template_file = shift;
	my $target_file = shift;


#print "In process_tempalte_file trying to output from $template_file to $target_file using cat $curcat\n";

	my $min_interest = 0;  # for images
        my $img_small = 1;     # small random images
	if ($curcat eq 301) {
		$min_interest = $MIN_FRONTPAGE_INTEREST;
	}

	# use macros for some vars, and for replacing output
	my $abm;
	$abm = new AbMacros(catid=>$curcat,abdomain=>$abdomain);
	
	# initialize templatehash
	my %templatehash = ();

	my $catcode  = &AbUtils::get_catcode($curcat);
        my $carr = &AbUtils::ArrayFromCatCode($catcode);
        my $lvl = &AbUtils::GetLevel($carr)+1;


	my $catref = new AbCat($curcat);
	$HAVECATS{$curcat} = $catref;
	my $catpath = $catref->make_nice_catpath($rootdom);
#print "Nice path for $catref->{'NAME'} is $catpath\n";
	# refresh templatehash

	$catowner = &AbUtils::get_catowner($curcat);  # null owner will default to our ads

	my @subcats = ();

	### Get a cat image, if any
	my $catimg_ref = &AbUtils::get_catimg($curcat, $lvl, $PUBLIC_ACCESS_LEVEL);

	### Getting subcats of $curcat
	&AbUtils::get_subcats($curcat, \@subcats, $userid, $MAX_SUBCATS);  

	my @relcats = ();

	### Getting related categories 
	&AbUtils::get_relcats($curcat, \@relcats, $userid);

	&AbUtils::fmt_array_for_table(\@subcats, 2);	# 2-column table for use in left-side column

	my @blogitems = ();
	
	### Getting blogitems
# get_all_blogitems {        my $curcat = shift;        my $lvl = shift;        my $itemref = shift;
#        my $max_security_level = shift || 0;
#        my $min_importance = shift || 0;
#        my $min_bloglength = shift || 10;
#        my $max_items = shift || 60;
#        my $hide_hidden = shift || 0;

        my $hide_hidden = 0;
        if ($curcat == $DEFAULT_CAT) {
          $hide_hidden = 1;
        }

	&AbUtils::get_all_blogitems($curcat, $lvl, \@blogitems,$PUBLIC_ACCESS_LEVEL, $COMMENT, 10, 60, $hide_hidden);

        my @featureitems = ();

        ### Getting featureitems
        $MIN_FEATURE_LENGTH = 50;
        $MAX_FEATURE_ITEMS = 25;
        $PERMANENT_ITEM = 30;
        &AbUtils::get_all_featureitems($curcat, $lvl, \@featureitems,$PUBLIC_ACCESS_LEVEL, $COMMENT,$MIN_FEATURE_LENGTH, $MAX_FEATURE_ITEMS);
print "IN abmakev, we have ",$#featureitems, " feature items and permanent_item = $PERMANENT_ITEM****\n";
	my @catitems = (); 

	### Getting catitems
	&AbUtils::get_catitems($curcat, $lvl, \@catitems, $PUBLIC_ACCESS_LEVEL, $PERMANENT_ITEM, $MAX_ITEMS, $MAX_ITEM_LENGTH);

	## Sorting catitems
	eval {
	    @catitems = sort { $a->{'NAME'} cmp $b->{'NAME'} } @catitems;
	};

print "We have ",$#catitems," catitems for $curcat\n";

#	my @catrelated = ();
#	&AbUtils::get_relations($curcat, 'category', 'ALL', \@catrelated);
#	&AbUtils::fmt_array_for_table(\@catrelated, 5);	# 5-column table

	### fixing up catitems

	################
	# TODO move this whole section into AbMacros
	# fixup possible bad data
	$lastmod = 0;
	foreach my $itemref (@catitems) {
		# don't use malformed URLs
		if ($itemref->{'LINK'} !~ /^http/) {
			$itemref->{'LINK'} = '';
		}
		# TODO move to abutils
		$itemref->{'ITEMLINK'} = $catref->{'REL_URL'}.'/'.$itemref->{'ID'};
		$itemref->{'EDITLINKS'} = $abm->EditLinks($itemref->{'ID'}, $itemref->{'NAME'});
		$itemref->{'DISPLAY_URL'} = substr($itemref->{'URL'},0,$MAX_URL_DISPLAY_LENGTH);
		$itemref->{'THUMBNAIL'} = $abm->MakeThumbnail($itemref->{'ID'});
	}
	
	### fixing up blogitems
        &AbUtils::simple_fixup_items(\@blogitems);
        &AbUtils::simple_fixup_items(\@featureitems);
	
	foreach my $itemref (@blogitems) {
		# don't use malformed URLs
		if ($itemref->{'LINK'} !~ /^http/) {
			$itemref->{'LINK'} = '';
		}
		if ($itemref->{'HAVE_MORE'}) {
			$itemref->{'MORELINK'} = "<A HREF='".$itemref->{'ITEMLINK'}."'>... read more</A>";
		}

		$itemref->{'THUMBNAIL'} = $abm->MakeThumbnail($itemref->{'ID'});
		$itemref->{'DISPLAY_URL'} = substr($itemref->{'URL'},0,$MAX_URL_DISPLAY_LENGTH);
	}
	##################


	### Fixing subcats 
        
	foreach my $subcatref (@subcats) {
		$subcatref->{'CATLINK'} = $subcatref->{REL_URL};
#print "for SUBCAT ",$subcatref->{'NAME'}," ID ",$subcatref->{'ID'}," nice catpath is ",$subcatref->{'CATLINK'}, "\n";
		$subcatref->{'ITEMLINKS'} = $abm->CatItemsBrief($subcatref->{'ID'}, $subcatref->{REL_URL});
		$subcatref->{'SUBSUBCATS'} = $abm->SubcatsItemsBrief($subcatref->{'ID'});

	}


	### Fixing relcats 

# TODO: condense identical cats in different parent cats - in db?

	foreach my $subcatref (@relcats) {
		$subcatref->{'CATLINK'} = $subcatref->{REL_URL};
print "for RELCAT ",$subcatref->{'NAME'}," ID ",$subcatref->{'ID'}," nice catpath is ",$subcatref->{'CATLINK'}, "\n";
		$subcatref->{'ITEMLINKS'} = $abm->CatItemsBrief($subcatref->{'ID'}, $subcatref->{REL_URL});
		$subcatref->{'SUBSUBCATS'} = $abm->SubcatsItemsBrief($subcatref->{'ID'});

	}


	$templatehash{'FEATURE'} = $abm->Feature($curcat);
	$templatehash{'GOOGLE_AD_CODE'} = $abm->GoogleAdCode($catowner);
	$templatehash{'SUBCATS'} = \@subcats;
	$templatehash{'RELCATS'} = \@relcats;
	$templatehash{'CATITEMS'} = \@catitems;
	$templatehash{'FEATUREITEMS'} = \@featureitems;
	$templatehash{'BLOGITEMS'} = \@blogitems;
	# $templatehash{'ITEMRELATIONS'} = \@itemrelated;
	# $templatehash{'CATRELATIONS'} = \@catrelated;
	@relation_names = ();
	foreach my $mrel (keys(%RELATIONS)) {
		my $href = {'NAME'=>$mrel};
		push @relation_names, $href;
	}
	$templatehash{'RELATIONS'} = \@relation_names;
	$templatehash{'CATPATH'} = $catpath;
	$templatehash{'MENUDIVS'} = $abm->MenuDivs;
#	$templatehash{'DIVCATPATH'} = $abm->DivCatPath(2,'/Tucson/');
	$templatehash{'DIVCATPATH'} = $abm->DivCatPath(1);
	$templatehash{'CATNAME'} = $abm->makeSafeStr($catref->{'NAME'});

	if ($abm->want_events($catref->{'NAME'})) {
print "*** want events\n";
		$templatehash{'EVENTS'} = $abm->get_events_by_keyword($catref->{'NAME'});
	}
       $templatehash{'SIDEBAR_IMGS'} = $abm->SideBarImgs();


	$templatehash{'CATCODE'} = &AbUtils::catcodestr($catref->{'CATCODE'});
	$templatehash{'CATID'} = $curcat;

#        my $fq = "select fwix_id from fwix_cats where cid = $curcat";
#        my ($fwixid) = $dbh->selectrow_array($fq);
#        if ($fwixid) {
#           $templatehash{'FWIXFEED'} = $abm->makeFwixFeed($fwixid); # TODO HERE see http://fwix.com/demos/api_example/fetch_stories.html
#        }



	$templatehash{'ITEMID'} = $curitem;
	$templatehash{'CATIMG'} = $abm->CatImg($catimg_ref);
	$templatehash{'CAT_IMGS'} = $abm->RandCatImgs($curcat, $lvl, $PUBLIC_ACCESS_LEVEL,$MAX_SHOW_IMGS, $min_interest);
        my $use_sm_images = 1;
	$templatehash{'SM_CAT_IMGS'} = $abm->RandCatImgs($curcat, $lvl, $PUBLIC_ACCESS_LEVEL,$MAX_SHOW_IMGS, $min_interest, $use_sm_images);

	$templatehash{'SQUARE_IMGS'} = $abm->RandImgSquare($curcat, $lvl, $PUBLIC_ACCESS_LEVEL,$NUM_SQUARE_IMGS, $min_interest);
#	$templatehash{'THISCGI'} = $THISCGI;
	$templatehash{'BLOGCGI'} = $BLOGCGI;
	$templatehash{'USERPREF'} = $userpref;
	$templatehash{'THISLINK'} = $catref->{'REL_URL'};
	$templatehash{'NEXTPAGE'} = $nextpage;
	$templatehash{'SHOW_LOGIN'} = $User eq '' ? 1 : 0;
	$templatehash{'LOGINLINK'} = $abm->LoginOrWelcome($catref->{'REL_URL'});
	$templatehash{'REGISTERLINK'} = "<A HREF=\"".$REGISTERURL."\">register</A>";
	$templatehash{'ACCOUNTLINK'} = "<A HREF=\"".$ACCOUNTURL."\">my account</A>";
	$templatehash{'ABTYPES'} = \@ABTYPES;

        my $catname = $catref->{'NAME'};
	# HACK for now
	my $preblogcode = '';

	if ($curcat == 301) {   # On the home page we don't use a scrollbox, at least for now
                $preblogcode = '<div class="homeblog">';
                $fpreblogcode = '<div class="featblog">';

        } else {
                $preblogcode = '<div class="sblog">
<div class="sbloghead">What\'s new with '.$catname.' <span style="float:right"><a class="bloghead" href="javascript:ab_show_popwin(\'placeAddForm\',\'/inc/add_to_cat.php?CATID='.$curcat.'&CATNAME='.$catname.'\')"><small>add item</small></a></span></div>';
	}
        my $headline_precode = '<div class="feat_headlines">';

	# optional preblogcode for adding extra content to page

	### Making BlogRoll
# depends on other templatehash fields
        print "Making blogroll: ***********\n";
	$templatehash{'BLOGROLL'} = $abm->BlogRoll(\@blogitems,\%templatehash, $preblogcode);
        print "Done with blogroll: *******\n";
        ### May later treat features differently, for now do same thing as for blogroll

        $templatehash{'FEATURE_ROLL'} = $abm->FeatureRoll(\@featureitems, \%templatehash, $fpreblogcode);
        $templatehash{'FEATURE_HEADLINES'} = $abm->FeatureHeadlines(\@featureitems, \%templatehash, $headline_precode);


#	if ($curitem) {
#        	$templatehash{'ITEMNAME'} = $iref->{'NAME'};
#	        $templatehash{'ITEMVALUE'} = &AbUtils::html_quotes($iref->{'VALUE'});
#        	$templatehash{'ITEMDESC'} = &AbUtils::html_quotes($iref->{'DESCRIPTION'});
#		$templatehash{'ITEMCODE'} = &AbUtils::catcodestr($iref->{'ITEMCODE'});
#	}


	$templatehash{'META_DESCRIP'} = $abdomain->makeCatMetaDesc($catref, \@subcats,\@relcats, \@catitems, \@blogitems);

	# we iterate on $template_file

	# Processing the template file
	my $tmpstring = $abm->ProcessFile($template_file);

	# now output to corresponding .html (warn on overwrite?)

	&CommandWeb::OutputToFileFromString($tmpstring,$target_file,\%templatehash) || warn("CommandWeb::OutputToWeb failed writing to $target_file, last error was $?, hash was ",%templatehash);

        `chown abupdate '$target_file'`;

} # end processtemplatefile


1;






sub prompt {
        my($prompt,$def) = @_;
        $prompt = &subvars($prompt);
        if ($def) {
                if ($prompt =~ /:$/) {
                        chop $prompt;
                }
                if ($prompt =~ /\s$/) {
                        chop $prompt;
                }
                print $prompt," [",$def,"]: ";
        } else {
                if ($prompt !~ /[:\?]\s*$/) {
                        $prompt .= ': ';
                } elsif ($prompt !~ /\s$/) {
                        $prompt .= ' ';
                }
                print $prompt;
        }
        $| = 1;
        $_ = <STDIN>;
        chomp;
        return $_?$_:$def;
}

