/**
 * Created by Mateuszek on 18.12.14 10:33.
 * https://github.com/mateuszdargacz
 */

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

      nicEditors.allTextAreas(nicedit_options);



});
