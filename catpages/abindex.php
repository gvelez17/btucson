<?php
 
$mobile_browser = 0;
 
if(preg_match('/(up.browser|up.link|mmp|symbian|smartphone|midp|wap|phone)/i', strtolower($_SERVER['HTTP_USER_AGENT']))) {
    $mobile_browser = 1;
}
 
if((strpos(strtolower($_SERVER['HTTP_ACCEPT']),'application/vnd.wap.xhtml+xml')>0) or ((isset($_SERVER['HTTP_X_WAP_PROFILE']) or isset($_SERVER['HTTP_PROFILE'])))) {
    $mobile_browser = 1;
}    
 
$mobile_ua = strtolower(substr($_SERVER['HTTP_USER_AGENT'],0,4));
$mobile_agents = array(
    'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
    'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
    'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
    'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
    'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
    'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
    'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
    'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
    'wapr','webc','winw','winw','xda','xda-');
 
if(in_array($mobile_ua,$mobile_agents)) {
    $mobile_browser = 1;
}
 
if (strpos(strtolower($_SERVER['ALL_HTTP']),'OperaMini')>0) {
    $mobile_browser = 1;
}
 
$ua = strtolower($_SERVER['HTTP_USER_AGENT']);

if (strpos($ua,'windows')>0) {
    $mobile_browser=0;
}

//treat IE 6.0 as a mobile browser
if ((strpos($ua,'msie 6.0')>0)  && (strpos($ua,'opera')<=0) ) {
   $mobile_browser=1;
}

print "<!-- ua was $ua , mobile_ua is $mobile_ua , mobile_browser is $mobile_browser -->\n";
 
if($mobile_browser) {
	include("ab_mobile.php");   
}
else {
   include ("abra.php");
}   
 
?>
<!-- modified from http://mobiforge.com/developing/story/lightweight-device-detection-php -->
