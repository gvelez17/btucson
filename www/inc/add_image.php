<?
        session_start();
?>

<!-- image upload form -->

<!-- used by /templates/301.tmpl and js2/ab_utils.js  -->

<link href="/boxy.css" rel="styleSheet" type="text/css">

<script type="text/javascript" src="/js2/ab_utils.js"></script>

<A HREF="javascript:ab_hide_popwin('placeAddForm')">X : <small>hide form</small></A>
<br>
Upload your images here!  Note, due to security concerns only logged in users may upload images.
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

<FORM ENCTYPE="multipart/form-data" action="/cgi/loadimg.pl" method=post>

<input name="_reply" type=hidden value="http://bTucson.com/thankyou.php">

<div id=formarea>
You are uploading an image related to the item:
<? 
print '<b>'.$ITEMNAME.'</b>'; 
print '<input type=hidden name="_catid" value="';
print $CATID;
print '">';
print '<input type=hidden name="_related_to_item" value="';
print $ITEMID;
print '">';
?>

Please select an image file to upload: 
<BR> 
<INPUT TYPE="FILE" NAME="image_file">
<br>
<input type=HIDDEN name="rank" value=20>
Credits : <input name="credits" size=25>
<br>
Caption :<br>
<textarea rows=3 cols=50 name="caption"></textarea>
<p>
<?
if (!isset($_SESSION['user'])) {
        print 'Guest posts welcome - if you are a human, please finish this line: <i>Humpty Dumpty sat on a <input name="human_check_1" size=4 maxlength=4></i><p>';
}
?>

<input type=submit value="Click to Post">
<p>

<small>Please respect our users. This site is meant to help people find information about Tucson. Negative comments are ok, but please keep them concrete and reasonable.</small><p>

<small>Problems or questions?  <A HREF="http://webglimpse.net/contact.php">contact us here</A>.</small>
</FORM>
