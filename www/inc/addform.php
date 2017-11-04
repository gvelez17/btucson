<?
        session_start();
?>
<link href="/2col.css" rel="styleSheet" type="text/css">
<script type="text/javascript" src="/js/ab_scripts.js"></script>

Add information to this site!  Just <b>choose a category</b> and type what you have to say.  You can post items even if you are not registered, but they will only show up after editor approval.
<br>

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
<FORM action="/cgi/blogform.pl" method=post>

<input name="_reply" type=hidden value="http://bTucson.com/">


<div id=formarea>
Give your post a title : <input name="title" size=25>
<br>
Choose a category:
<br>
<SELECT name="_catid" SIZE=9>
<OPTION value=306> Business Directory
<OPTION value=303> Community Info
<OPTION value=309> Economic Info
<OPTION value=307> Housing
<OPTION value=302> News
<OPTION value=304> Parks & Rec
<OPTION value=310> Politics & Government
<OPTION value=305> Restaurant Guide
<OPTION value=308> Schools & Universities
</SELECT>
<br>
Your notes, comments, or observations here:<br>
<textarea rows=8 cols=50 name="SHORT_CONTENT"></textarea>
<br>
Is there a URL that relates to this item? <br>
<input name="url" size=50>
<p>
<?
if (!isset($_SESSION['user'])) {
        print 'Guest posts welcome - if you are a human, please finish this line: <i>Humpty Dumpty sat on a <input name="human_check_1" size=4 maxlength=4></i><p>';
}
?>

<input type=submit value="Click to Post">
<p>

<small>Please respect our users. This site is meant to help people find information about Tucson, please use it appropriately.</small><p>

<small>Problems or questions?  <A HREF="http://webglimpse.net/contact.php">contact us here</A>.</small>
</FORM>
