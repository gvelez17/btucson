<?
        session_start();
?>

<!-- comment form -->

<!-- used by /templates/301.tmpl and js2/ab_utils.js  -->

<link href="/boxy.css" rel="styleSheet" type="text/css">

<script type="text/javascript" src="/js2/ab_utils.js"></script>

<A HREF="javascript:ab_hide_popwin('placeAddForm')">X : <small>hide form</small></A>
<br>
Add your comment here!  You can post comments even if you are not registered, but they will only show up after editor approval.
&nbsp;&nbsp;&gt;&gt;&gt;
<span style="font-weight:500;"><i>Please be concrete</i>, and if possible indicate your basis for making the comment.  Are you a customer, the business owner, an employee or other?   </span>
<p>

<p>
<?
if (isset($_SESSION['user'])) {
        print "<small>welcome ".$_SESSION['user']."</small><br>"; 
}
?>

<FORM action="/cgi/blogform.pl" method=post>

<input name="_reply" type=hidden value="http://bTucson.com/thankyou.php">

<div id=formarea>
You are posting a comment related to the item:
<? 
print '<b>'.$ITEMNAME.'</b>'; 
print '<input type=hidden name="_catid" value="';
print $CATID;
print '">';
print '<input type=hidden name="_related_to_item" value="';
print $ITEMID;
print '">';
?>
<br>
<input type=HIDDEN name="rank" value=20>
Give your comment a descriptive headline : <input name="title" size=25>
<br>
Enter your notes, comments, or observations about this listing below.  
<? if (!isset($_SESSION['user'])) {
	print "We encourage you to sign your name, but its not required.";
   }
?>
<br>
<textarea rows=8 cols=80 name="SHORT_CONTENT"></textarea>
<br>
<small>Please respect our users. This site is meant to help people find information about Tucson. Negative comments are ok, but please keep them specific and reasonable.


Generic 'great!' or 'terrible!' type comments will generally be deleted unless you include some supporting details and indicate how you fit into the picture.  
  </small><p>
Is there a URL that relates to your comment? <input name="url" size=30>
<br>
<?
if (!isset($_SESSION['user'])) {
        print 'Guest posts welcome<br>';
	print ' * TO VERIFY THAT YOU ARE HUMAN * <br>Please fill out the rest of this sentence: <i>Humpty Dumpty sat on a <input name="human_check_1" size=4 maxlength=4></i><p>';
}
?><br>
<small>by clicking the following button you confer to bTucson.com rights to publish, edit and otherwise use the above text</small><br>
&gt;&gt;<input type=submit value="Click to Post">&lt;&lt;&nbsp;&nbsp;<small>
<b>NOTE: </b> this is NOT a way to communicate with listed businesses.  Your comment will (probably) appear on the bTucson.com website, but there is no guarantee who will see it. </small> 
<br>
<b>Thank you for sharing!</b>
<p>


<small>Problems or questions?  <A HREF="http://webglimpse.net/contact.php">contact us here</A>.</small>
</FORM>
