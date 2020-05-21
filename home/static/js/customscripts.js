// custom jquery scripts

$(document).ready(

    // the following scripts apply to the homepage




    //the following scripts are for the modals @ homepage
    function() {

        $("#forgotten").click(function() {
            $(".modal-footer-forgot").show().slideDown();
            $("#loginId").hide();


        });
        $("#forgotten").click(function() {
            $("#signUpId").toggle();

        });

        //    $("#signUpId").click(function(){
        //     $("#loginModal").hide();

        //    });


    });