/**
 * Created by Mateuszek on 18.12.14 10:33.
 * https://github.com/mateuszdargacz
 */
"use strict";

$(document).ready(function () {

    var comment_text_area_id = 'id_comment',
        comment_text_area = $('#' + comment_text_area_id),
        modal_sel = '#comment_login',
        modal_options = {

        },
        //        modal = $(modal_sel).modal(modal_options),
        nicedit_options = {
            buttonList: ['bold', 'italic', 'underline', 'ol', 'ul']
        };

    var edit = new nicEditor(nicedit_options).panelInstance(comment_text_area_id);
    //    Remove styles added by nicedit
    $('.nicEdit-main').parent().removeAttr('style');
    $('.nicEdit-a').removeAttr('style');
    //    END Remove styles added by nicedit

    $('#edit_btn').on('click', function(e){
        e.preventDefault();
        $('.nicEdit-edit_bar').toggle();
    });

});
