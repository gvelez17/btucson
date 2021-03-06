POPUP_DELAY = 100;   // milliseconds after mouseover for popup menu
BASE_ZINDEX = 500;

mX = 0;
mY = 0;

mXOffset = 30;
mYOffset = 15;

COMMENT_BOX_Y_OFFSET = 50;

old_parent_zindex = 0;	// global

M_LEVELS = 5;
SUBMENUS = [];

function verify_captcha(mform) {
    if ( (mform.logged_in_user.value != 1) && (mform.human_check_1.value != 'wall') ) {
        alert("Please complete the \'Are you human?\' question before submitting");
        return false;
    }
    return true;
}

function rearrange_if_wide () {
	
	ad_code_div = document.getElementById("topAdCode");

	left_nav_div = document.getElementById("leftNavBar");

        w = 0;
        if (window.width) {
                w = window.width;
        } else if (window.innerWidth) {
                w = window.innerWidth;
        } else if (document.body.clientWidth) {
                w = document.body.clientWidth;
        }
	if (w > 930) {
//		ad_code_div.style.margin = '0 0 0 203px';
		ad_code_div.style.left = '203px';
		left_nav_div.style.top = 0;
	}

}


function ab_init_menus () {

	for (j=1; j<M_LEVELS+1; j++) {
 		mid = 'menu_level_' + String(j);

        	SUBMENUS[j] = document.getElementById(mid);
	}

}

function ab_have_session () {
        var allcookies = document.cookie;

        var pos = allcookies.indexOf("PHPSESSID=");

        if (pos == -1) {
                return false;
        } else {
                return true;
        }
}


function ab_set_timer_cascade(elem,evnt,catcode,is_top_level) {
	
	var timer;

	// COULD START LOADING DATA NOW if we want - make behavior really slick!

	mX = evnt.clientX;
	mY = evnt.clientY;


	// the event is the mouseover the menu element
	if (is_top_level) {
		timer = window.setTimeout(function() { 
		 	ab_top_cascade(elem, catcode); 
		}, POPUP_DELAY);
	} else {
		timer = window.setTimeout(function() {
			ab_cascade(elem, catcode);
		}, POPUP_DELAY);
	}	

	// code supporting multiple browsers from O'Reilly JS book rev 5 p 420
	if (elem.addEventListener) { elem.addEventListener("mouseout", ab_cancel_timer, false); }
	else if (elem.attachEvent) { elem.attachEvent("onmouseout", ab_cancel_timer); }
	else { elem.onmouseout = ab_cancel_timer; }

	function ab_cancel_timer() {
		window.clearTimeout(timer);
		if (elem.removeEventListener) {
			elem.removeEventListener("mouseout",ab_cancel_timer, false);
		} else if (elem.detachEvent) { elem.detachEvent("onmouseout",ab_cancel_timer); }
		else { elem.onmouseout = null; }

		// turn progress cursor off
		// cursor = pointer
		// thislink not defined
		elem.setAttribute("style","cursor: pointer;");
	}			
}


function ab_remove_panel(mlink) {
        var mpanel = mlink.parentNode.parentNode; 
        if (mpanel) {
                 mlevelstr = mpanel.getAttribute("level");
        	if (mlevelstr){
                	mlevelnum = parseInt(mlevelstr) + 1;
	        } else {
        	        mlevelnum = 1;
		}
		for (x = mlevelnum; x<M_LEVELS; x++) {
			if (SUBMENUS[x]) {
				SUBMENUS[x].style.display = 'none';
			}
		}

		mpanel.style.display = 'none';		
        }
}

function ab_top_cascade(thislink, catcode) {
	//ab_remove_all();
	ab_cascade(thislink, catcode);
}

function ab_cascade(thislink, catcode) {

	mparent = thislink.parentNode;

	mlevelstr = mparent.getAttribute("level");
//alert("Raw level of parent is " + mlevelstr);
	if (mlevelstr){
		mlevelnum = parseInt(mlevelstr) + 1;
	} else {
		mlevelnum = 1;
	}

	// Hide any menus lower than our current level
	for (x = mlevelnum+1; x<=M_LEVELS; x++) {
		if (SUBMENUS[x]) {
			SUBMENUS[x].style.display = 'none';
		}
	}


	mzindex = BASE_ZINDEX + mlevelnum *10;

	mpop = SUBMENUS[mlevelnum];
	
	mpop.style.zIndex = mzindex;

	// Could move into position based on mparent
	// here we use the coords of the mouse event
	if (mlevelnum > 1) {
		m_menu_parent = SUBMENUS[mlevelnum - 1];
		mX = parseInt(m_menu_parent.style.left) + mXOffset;
		mY = parseInt(m_menu_parent.style.top) + mYOffset;
	}
	mParentX = mpop.parentNode.style.left;
	mParentY = mpop.parentNode.style.top;
	
	mXOff = (mX - mParentX);
	mYOff = (mY - mParentY);

	mStrX = String(mX) + 'px';
        mStrY = String(mY) + 'px';

//alert ("left was " + mpop.style.left + " now setting to " + mStrX);
	mpop.style.left = mStrX;  // was mXOff
	mpop.style.top = mStrY;  // was mYOff

        fill_elem_from_catcode (mpop, catcode);

	mpop.style.display = 'block';
}


function fill_elem_from_catcode ( fill_elem, catcode ) {
       // var dataurl = "http://btucson.com/inc/cats2/" + catcode + ".html";
       var dataurl = "/inc/cats2/" + catcode + ".html";
        var myAj = new Ajax.Updater(
                fill_elem,
                dataurl,
                {
                        method: 'get'
                }
        );

		// TODO: callback to turn progress off after data loaded

		// TODO TODO  - also should only set display=block AFTER correct data loads

		// turn progress cursor off
		// cursor = pointer
		//thislink.setAttribute("style","cursor: pointer;");

}

function ab_hide_popwin (elemname) {
        $(elemname).style.visibility = 'hidden';
}

function ab_show_popwin(elemname, content_url ) {

        $(elemname).style.visibility = 'visible';

        var myAj = new Ajax.Updater(
                $(elemname),
                content_url,
                {
                        method: 'get'
                }
        );
}

function ab_move_and_show_popwin(elemname, content_url) {

//        var my_pop_elem = document.getElementByName(elemname);

//      if (my_win_elem.offsetLeft > 0) {
 //             myX = parseInt(my_win_elem.offsetLeft) + mXOffset;
 //             myY = parseInt(my_win_elem.offsetTop) + mYOffset;
 //               } else {
 //               // we are using mouse coords, may have to offset for window scroll
 //                       mY = mY + getScrollY();
 //               }
 //       mStrX = String(mX) + 'px';
 //       mStrY = String(mY) + 'px';

	var my_pop_elem = $(elemname);
	var yscroll = getScrollY();
        top_coord = COMMENT_BOX_Y_OFFSET + yscroll;
        mStrY = String(top_coord) + 'px';

//alert("Scroll is " + yscroll + " setting top to " + mStrY);
        my_pop_elem.style.top = mStrY;

        ab_show_popwin(elemname, content_url);
}

// from http://www.howtocreate.co.uk/tutorials/javascript/browserwindow
function getScrollY() {
  var scrOfX = 0, scrOfY = 0;
  if( typeof( window.pageYOffset ) == 'number' ) {
    //Netscape compliant
    scrOfY = window.pageYOffset;
    scrOfX = window.pageXOffset;
  } else if( document.body && ( document.body.scrollLeft || document.body.scrollTop ) ) {
    //DOM compliant
    scrOfY = document.body.scrollTop;
    scrOfX = document.body.scrollLeft;
  } else if( document.documentElement && ( document.documentElement.scrollLeft || document.documentElement.scrollTop ) ) {
    //IE6 standards compliant mode
    scrOfY = document.documentElement.scrollTop;
    scrOfX = document.documentElement.scrollLeft;
  }
//  return [ scrOfX, scrOfY ];
  // just for now to test
  return scrOfY;
}

function showLogin () {

	$('login_form').style.display = 'block';
}

function hideAddForm () {
        $('placeAddForm').style.display = 'none';
}

function showAddForm(formurl) {

        if ($('placeAddForm').style.display == 'none') {
                $('placeAddForm').style.display = '';
        } else {
                var myAj = new Ajax.Updater(
                        $('placeAddForm'),
                        formurl,
                        {
                                method: 'get'
                        }
                );
        }
}

// from www.daniweb.com/techtalkforums/thread45103.html
function addBookmark(title, url) {
        if (window.sidebar) { // firefox
              window.sidebar.addPanel(title, url,"");
        } else if( window.external ) { //MSIE
                window.external.AddFavorite( url, title);
        } else {
               alert("Sorry, your browser doesn't support this");
        }
}
 
