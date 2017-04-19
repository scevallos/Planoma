// window.onload = function () {
//     var on_mouse_over = function() {
//         this.className = this.className + " hovered";
//     };
//     var on_mouse_out = function() {
//         this.className = this.className.replace( /(?:^|\s) hovered(?!\S)/g , '');
//     }
//     var items = document.getElementsByTagName('li');
//     for(var i = 0; i < items.length; i++) {
//         items[i].addEventListener('mouseover', on_mouse_over);
//         items[i].addEventListener('mouseout', on_mouse_out);
//     }
// };
var IS_ARCHIVE = 1;
    
function initFlyouts(){
    initPublishedFlyoutMenus(
        [{"id":"617861647785568713","title":"Home","url":"index.html","target":"","nav_menu":false,"nonclickable":false},{"id":"460448653247643812","title":"My Schedules","url":"my-schedules.html","target":"","nav_menu":false,"nonclickable":true},{"id":"399140095119712199","title":"Account","url":"account.html","target":"","nav_menu":false,"nonclickable":true},{"id":"223160214585533492","title":"Contact Us","url":"contact-us.html","target":"","nav_menu":false,"nonclickable":false}],
        "617861647785568713",
        '',
        'active',
        false,
        {"navigation\/item":"<li {{#id}}id=\"{{id}}\"{{\/id}} class=\"wsite-menu-item-wrap\">\n\t<a\n\t\t{{^nonclickable}}\n\t\t\t{{^nav_menu}}\n\t\t\t\thref=\"{{url}}\"\n\t\t\t{{\/nav_menu}}\n\t\t{{\/nonclickable}}\n\t\t{{#target}}\n\t\t\ttarget=\"{{target}}\"\n\t\t{{\/target}}\n\t\t{{#membership_required}}\n\t\t\tdata-membership-required=\"{{.}}\"\n\t\t{{\/membership_required}}\n\t\tclass=\"wsite-menu-item\"\n\t\t>\n\t\t{{{title_html}}}\n\t<\/a>\n\t{{#has_children}}{{> navigation\/flyout\/list}}{{\/has_children}}\n<\/li>\n","navigation\/flyout\/list":"<div class=\"wsite-menu-wrap\" style=\"display:none\">\n\t<ul class=\"wsite-menu\">\n\t\t{{#children}}{{> navigation\/flyout\/item}}{{\/children}}\n\t<\/ul>\n<\/div>\n","navigation\/flyout\/item":"<li {{#id}}id=\"{{id}}\"{{\/id}}\n\tclass=\"wsite-menu-subitem-wrap {{#is_current}}wsite-nav-current{{\/is_current}}\"\n\t>\n\t<a\n\t\t{{^nonclickable}}\n\t\t\t{{^nav_menu}}\n\t\t\t\thref=\"{{url}}\"\n\t\t\t{{\/nav_menu}}\n\t\t{{\/nonclickable}}\n\t\t{{#target}}\n\t\t\ttarget=\"{{target}}\"\n\t\t{{\/target}}\n\t\tclass=\"wsite-menu-subitem\"\n\t\t>\n\t\t<span class=\"wsite-menu-title\">\n\t\t\t{{{title_html}}}\n\t\t<\/span>{{#has_children}}<span class=\"wsite-menu-arrow\">&gt;<\/span>{{\/has_children}}\n\t<\/a>\n\t{{#has_children}}{{> navigation\/flyout\/list}}{{\/has_children}}\n<\/li>\n"},
        {"hasCustomMinicart":true}
    )
}