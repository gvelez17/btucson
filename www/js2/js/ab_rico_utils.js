
function ab_expand(container_elem, fill_elem, catcode) {
	// insert data into content div
	new Rico.Accordion( $(container_elem) );

	// change ++ to -- icon

	// retrieve data and insert into fill_elem
	fill_elem_from_catcode (fill_elem, catcode);
}

function add_accordion_node_from_link(this_link, catcode) {

alert ('name is ' + this_link.getAttribute('name'));

	var panel_elem = this_link.parentNode.parentNode;
	var new_elem_id = "subDivCat" + catcode;
	var newdiv = document.createElement("div");
	newdiv.setAttribute("id",new_elem_id);
	panel_elem.appendChild(newdiv);
	fill_elem_from_catcode(newdiv, catcode);
}

function fill_elem_from_catcode ( fill_elem, catcode ) {
       var dataurl = "http://btucson.com/inc/cats/" + catcode + ".html";
        var myAj = new Ajax.Updater(
                $(fill_elem),
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

	var my_submit = document.createElement("input");
	my_submit.value="Login";
	my_submit.name="Submit";
	my_submit.type="submit";

	my_login_form.appendChild(my_submit);

}
