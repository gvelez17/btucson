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

	// create the panel
	my_panel.id = "subMenu"+catcode;
	my_panel.value = parent_elem.value + 1;
	my_panel.style.position = "absolute";
   	my_panel.style.left = "2em";
   	my_panel.style.top = ".5em";
   	my_panel.style.height = "auto";
   	my_panel.style.width = "auto";
	my_panel.style.background = "#f0f8c0"; 
	my_panel.style.border = "solid";
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
       var dataurl = "http://btucson.com/inc/cats/" + catcode + ".html";
        var myAj = new Ajax.Updater(
                fill_elem,
                dataurl,
                {
                        method: 'get'
                }
        );

}

function hideAddForm () {
	$('placeAddForm').style.display = 'none';
	$('showAddFormText').style.display = '';
}

function showAddForm(formurl) {

	$('showAddFormText').style.display = 'none';
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

function showLogin () {
	
	var my_login_text = document.createTextNode("Username: ");
	var my_login_elem = document.getElementById("login_label");
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


	var my_login_text = document.getElementById("login_text");
	my_login_text.textContent = "";

	var my_reg_text = document.getElementById("reg_text");
	my_reg_text.textContent = "";

	var my_login_form = document.getElementById("login_form");		

	if (! my_login_form) {
		alert("Can't get element by id for login_form");
	}

	var my_submit = document.createElement("input");
	my_submit.value="Login";
	my_submit.name="Submit";
	my_submit.type="submit";

	if (! my_login_form.appendChild(my_submit)) {
		var my_submit_place = document.getElementById("submit_button");
		if (my_submit_place) {
			my_submit_place.appendChild(my_submit);
			alert("Had to use child");
		}
	}
}
