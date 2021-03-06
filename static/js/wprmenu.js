jQuery(document).ready(function(e) {
    var t = e("#wprmenu_bar"),
        n = t.outerHeight(true),
        r = t.attr("data-from_width"),
        i = e("#wprmenu_menu"),
        s = e("#wprmenu_menu_ul"),
        o = i.find("a"),
        u = e("body"),
        a = e("html"),
        f = 300,
        l = e("#wpadminbar"),
        c = t.length > 0 && i.length > 0 ? true : false,
        h = i.width(),
        p = window.innerHeight < u.height() ? u.height() : window.innerHeight,
        d = window.innerWidth < u.width() ? u.width() : window.innerWidth;
    if (c) {
        s.find("li").first().css({
            "border-top": "none"
        });
        e(document).mouseup(function(t) {
            if (!i.is(t.target) && i.has(t.target).length === 0) {
                if (i.is(":visible")) {
                    e.sidr("close", "wprmenu_menu")
                }
            }
        });
        i.find("ul.sub-menu").each(function() {
            var t = e(this),
                n = t.prev("a"),
                r = n.parent("li").first();
            n.addClass("wprmenu_parent_item");
            r.addClass("wprmenu_parent_item_li");
            var s = n.before('<span class="wprmenu_icon wprmenu_icon_par icon_default ' + i.attr("data-custom_icon") + '"></span> ').find(".wprmenu_icon_par");
            t.hide()
        });

        function v() {
            e(".wprmenu_parent_item_li").each(function() {
                var t = e(this),
                    n = 0,
                    r = t.find(".wprmenu_icon_par").first(),
                    o = t.find("a.wprmenu_parent_item").first();
                if (i.hasClass("top")) {
                    n = window.innerWidth
                } else {
                    n = s.innerWidth()
                }
                if (t.find(".wprmenu_clear").length == 0) o.after('<br class="wprmenu_clear"/>')
            })
        }
        v();
        e(".wprmenu_icon_par").on("click", function() {
            var t = e(this),
                n = t.parent("li").find("ul.sub-menu").first();
            n.slideToggle(300);
            t.toggleClass("wprmenu_par_opened");
            if (i.attr("data-custom_icon") != "") t.toggleClass(i.attr("data-custom_icon_open"));
            t.parent("li").first().toggleClass("wprmenu_no_border_bottom")
        });

        function m() {
            i.find("ul.sub-menu").each(function() {
                var t = e(this),
                    n = t.parent("li").find(".wprmenu_icon_par"),
                    r = t.parent("li");
                if (t.is(":visible")) t.slideUp(300);
                n.removeClass("wprmenu_par_opened");
                r.removeClass("wprmenu_no_border_bottom")
            })
        }
        var g = e("meta[name=viewport]");
        g = g.length ? g : e('<meta name="viewport" />').appendTo("head");
        if (i.attr("data-zooming") == "no") {
            g.attr("content", "user-scalable=no, width=device-width, maximum-scale=1, minimum-scale=1")
        } else {
            g.attr("content", "user-scalable=yes, width=device-width, initial-scale=1.0, minimum-scale=1")
        }
        if (e.browser.mozilla) {
            screen.addEventListener("orientationchange", function() {
                y()
            })
        } else {
            window.addEventListener("orientationchange", y, false)
        }

        function y() {
            window.scrollBy(1, 1);
            window.scrollBy(-1, -1);
            h = i.width();
            if (i.is(":visible") && i.hasClass("left")) {
                u.css({
                    left: h
                });
                u.scrollLeft(0)
            }
        }
        if (i.hasClass("left") || i.hasClass("right")) {
            var b = i.hasClass("left") ? "left" : "right";
            t.sidr({
                name: "wprmenu_menu",
                side: b,
                speed: f,
                onOpen: function() {
                    t.addClass("menu_is_opened")
                },
                onClose: function() {
                    t.removeClass("menu_is_opened");
                    m()
                }
            });
            o.on("click", function(t) {
                t.preventDefault();
                var n = e(this).attr("href");
                e.sidr("close", "wprmenu_menu");
                setTimeout(function() {
                    window.location.href = n
                }, f)
            });
            e("body").touchwipe({
                wipeLeft: function() {
                    e.sidr("close", "wprmenu_menu")
                },
                wipeRight: function() {
                    e.sidr("open", "wprmenu_menu")
                },
                preventDefaultEvents: false
            });
            e(window).resize(function() {
                d = window.innerWidth < u.width() ? u.width() : window.innerWidth;
                if (d > r && i.is(":visible")) {
                    e.sidr("close", "wprmenu_menu")
                }
            })
        } else if (i.hasClass("top")) {
            u.prepend(i);
            t.on("click", function(t) {
                e("html, body").animate({
                    scrollTop: 0
                }, f);
                m();
                i.stop(true, false).slideToggle(f)
            });
            o.on("click", function(t) {
                t.preventDefault();
                var n = e(this).attr("href");
                i.slideUp(f, function() {
                    window.location.href = n
                })
            });
            e(window).resize(function() {
                d = window.innerWidth < u.width() ? u.width() : window.innerWidth;
                if (d > r && i.is(":visible")) {
                    m();
                    i.slideUp(f, function() {})
                }
            })
        }
    }
})