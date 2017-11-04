<?
        session_start();
?>

<!-- inserted at bottom of category pages  -->



<hr>
Add information to this site!  You can post items even if you are not registered, but they will only show up after editor approval.
<br>
<small>
<?
if (isset($_SESSION['user'])) {
        print "<small>welcome ".$_SESSION['user']."</small> | <small><A HREF='/php/access_user/btucson.php?action=log_out&next_url=";
	print $_SERVER['REQUEST_URI'];
	print "'>logout</A><br>";
} else {
        include "/home/sites/iwtucson/www/inc/login_text.html";
	print '<form id="login_form" method=POST action="/php/access_user/login.php">';
	print '<input type=HIDDEN name="next_url" value="';
	print $_SERVER['REQUEST_URI'];
	print '">';
	print '<span id="login_label"></span>';
	print '<span id="passwd_label"></span>';
	print '</form>';
}
?>
</small>

<FORM action="/cgi/blogform.pl" method=post>

<input type=HIDDEN name="_REPLY" value="http://btucson.com/thankyou.php">  
<div id=formarea>
You are posting information under the category:
<? 
print '<b>'.$CATNAME.'</b>'; 
print '<input type=hidden name="_catid" value="';
print $CATID;
print '">';
?>
<br>
<small>Note: If you would like to comment about a specific item, please visit that item's detail page and use the 'Enter Comment' link.
</small>
<br>
<!--
Type of post: <SELECT name="itemtype">
<OPTION VALUE="comment" SELECTED> General note or information
<OPTION> Business/organization Listing
<OPTION> Personal home page or blog
<OPTION> Event
<OPTION> Job or volunteer position
<OPTION> Resume
</SELECT>
-->
<br>
Give your post a title : <input name="title" size=25>
<br>
Your notes, comments, or observations here:<br>
<textarea rows=8 cols=50 name="SHORT_CONTENT"></textarea>
<br>
Is there a URL that relates to this post? <br>
<input name="URL" size=50>
<p>
Public Contact information if applicable:<br>

Phone: <input name="TYPE:ab_biz_org:phone" size=25><br>
Address: <input name="TYPE:ab_biz_org:addr" size=25><br>
City: <input name="TYPE:ab_biz_org:city" size=15 value="Tucson"><br>
Zip: <input name="TYPE:ab_biz_org:zip" size=10>
<p>
Private Contact information for verification (optional, but encouraged):<br>
Your name: <input name="TYPE:ab_private:name" size=15> 
<br/>Your email: <input name="TYPE:ab_private:email" size=20>
or your phone: <input name="TYPE:ab_private:phone" size=15>

<p>
<?
if (!isset($_SESSION['user'])) {
        print 'Guest posts welcome - if you are a human, please finish this line: <i>Humpty Dumpty sat on a <input name="human_check_1" size=4 maxlength=4></i><p>';
}
?>

<input type=submit value="Click to Post">
<p>

<small>Please respect our users. This site is meant to help people find information about Tucson, please use it appropriately. <b>Directory-type sites</b> may add in the Business Directory and up to 2 other categories, and are asked to link back to http://bTucson.com. <b>SEO focused sites</b> may add entries, but are also asked to link back.</small><p>

<small>Problems or questions?  <A HREF="http://webglimpse.net/contact.php">contact us here</A>.</small>
</FORM>
