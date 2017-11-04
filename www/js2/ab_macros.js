// from www.daniweb.com/techtalkforums/thread45103.html

// Macros have specific text
function add_bTucson_comment_bookmark() {
	
	title = 'about Tucson page';
	url = "javascript:w=window.open('http://btucson.com/about/'+location,'abra_relate','left=20,top=20,width=800,height=700,location=yes,status=yes,resizable=yes,scrollbars=yes,toolbar=yes,menubar=yes');w.focus;void 0";

        if (window.sidebar) { // firefox
              window.sidebar.addPanel(title, url,"");
        } else if( window.external ) { //MSIE
                window.external.AddFavorite( url, title);
        } else {
               alert("Sorry, your browser doesn't support this");
        }
}


function make_upload_img_link(itemid, catid, san_url) {
    // thought I could add the FBID here, but can't.  will have to be in ab_show_popwin
    // leave this as a JS function, maybe later we can provide a way to turn the link on or off
    // depending on login status.  
    link = "javascript:ab_show_popwin('placeAddForm', '/inc/add_image.php?&ITEMID=" + itemid + "&CATID=" + catid + "&ITEMNAME=" + san_url + "')";
    document.getElementById('load_img_link').innerHTML = '<a href = "' + link + '">Upload Image</a>';
}
