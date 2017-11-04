POPUP_DELAY = 300;   // milliseconds after mouseover for popup menu

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




function ab_popdown(mpanel) {
	// remove any children of that element
        var children = mpanel.childNodes;
        for (var j=0; j < children.length; j++) {
                if (children[j].menu_part == "submenu") {
                        mpanel.removeChild(children[j]);
                }
        }
}
function ab_remove_panel(catcode) {
	var mpanel = document.getElementById("subMenu"+catcode);
	if (mpanel) {	
		ab_remove(mpanel);
	}
}

function ab_remove(mpanel) {
	ab_popdown(mpanel);
	if (mparent = mpanel.parentNode) {
		mparent.removeChild(mpanel);
	}
	delete mpanel;
}

function ab_remove_all() {
	var mtabs = document.getElementsByName('abTopMenu');
	for (var j=0; j< mtabs.length; j++) {
		ab_popdown(mtabs[j]);
	}
}

function ab_top_cascade(thislink, catcode) {
	ab_remove_all();
	ab_cascade(thislink, catcode);
}

function ab_cascade(thislink, catcode) {
	my_panel = document.createElement("div");
	parent_elem = thislink.parentNode;

	var mstyle = "";

	// create the panel
	my_panel.id = "subMenu"+catcode;
	
	my_parent_val =  Number(parent_elem.getAttribute("value"));
	if (! my_parent_val) {
		my_parent_val = 100;
	}

	my_val = 1 + my_parent_val;

	my_panel.setAttribute("value", my_val);

	mzindex = my_val * 10; 

	my_parent_left = Number(parent_elem.offsetLeft);
	if (! my_parent_left ) {
		my_parent_left = 40;
	}
	my_left = my_parent_left + 2;


	mstyle += "z-index: " + mzindex + "; ";  
	mstyle += "left: " + my_left + "em; top: 1.1em; height: auto; width: auto; ";
	mstyle += "position: absolute; ";
	mstyle += "background: #f0f8c0; ";
	mstyle += "opacity: 1.0; "; 
	mstyle += "border: solid 1px; ";
	mstyle += "padding: 0 0 0 3px; ";

	my_panel.setAttribute("style",mstyle);

	my_panel.menu_part = "submenu";

	// remove any other children of that parent element
	var children = parent_elem.childNodes;
	for (var j=0; j < children.length; j++) {
		if (children[j].menu_part == "submenu") {
			parent_elem.removeChild(children[j]);
		}
	}
	// add to parent, tell parent to have hide icon
	parent_elem.appendChild(my_panel);

//#TODO: lookup how to set bgcolor dynamically on panel
	parent_elem.setAttribute("background","#ddddbb");
	
	parent_popleft_id = "popleft_"+catcode;

	// TODO: add onclick popdown, div
	//popleft = document.getElementbyId(parent_popleft_id);
	//popleft.innerHTML = " - ";
	
	// hide parent's child of class ab_menu_expandable
	// show parent's child of class ab_menu_collapsable

	// retrieve data and insert into fill_elem
        fill_elem_from_catcode (my_panel, catcode);

}


function fill_elem_from_catcode ( fill_elem, catcode ) {
       var dataurl = "http://btucson.com/inc/cats2/" + catcode + ".html";
        var myAj = new Ajax.Updater(
                fill_elem,
                dataurl,
                {
                        method: 'get'
                }
        );

		// TODO: callback to turn progress off after data loaded
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

function showLogin () {
	
	var my_login_text = document.createTextNode("Username: ");
	var my_login_elem = document.getElementById("login_label");
	var my_button_elem = document.getElementById("login_button");
	my_login_elem.appendChild(my_login_text);

	var my_inp_login = document.createElement("input");
	my_inp_login.name = "login";
	my_inp_login.type = "text";
	my_inp_login_size = "20";

	my_login_elem.appendChild(my_inp_login);

	var my_login_br = document.getElementById("login_br");
	var my_br = document.createElement("br");
	if (my_login_br) {
		my_login_br.appendChild(my_br);
	}

	var my_passwd_text = document.createTextNode("Password: ");
	var my_passwd_elem = document.getElementById("passwd_label");
	my_passwd_elem.appendChild(my_passwd_text);

	//var my_login_form = document.getElementById("login_form");		

	//my_login_form.appendChild(my_inp_login);

	var my_inp_passwd = document.createElement("input");
	my_inp_passwd.name = "password";
	my_inp_passwd.type = "PASSWORD";
	my_inp_passwd_size = "20";

	my_passwd_elem.appendChild(my_inp_passwd);

	
	var my_submit = document.createElement("input");
	my_submit.value="Login";
	my_submit.name="Submit";
	my_submit.type="submit";

	my_button_elem.appendChild(my_submit);

	// add a 'Login' button
	var my_login_text = document.getElementById("login_text");
	my_login_text.textContent = "";

	var my_reg_text = document.getElementById("reg_text");
	my_reg_text.textContent = "";

	var my_login_form = document.getElementById("login_form");		

	if (! my_login_form) {
		alert("Can't get element by id for login_form");
	}


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
 
