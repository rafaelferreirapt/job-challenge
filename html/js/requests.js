$(document).ready(function () {
    $("#email_response").hide();
    $("#domain_response").hide();
});

var BASE_URL = "http://localhost:5001";

function domain() {
    $.ajax({
        url: BASE_URL + "/api/v1/domain/",
        type: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        data: JSON.stringify({"domain": $("#domain").val()}),
        success: function (data, textStatus, xhr) {
            $("#domain_response").show();

            if(data["result"].length==0){
                $("#domain_response").html("<h3>Your domain it's ok! Nothing found.</h3>");
            }else{
                var leaks = "";

                for (var i=0; i<data["result"].length; i++){
                    leaks += " " + data["result"][i] + ",";
                }

                $("#domain_response").html("<h3>Your domain is in the following leaks:"+leaks.slice(0, -1)+"</h3>");
            }
        },
        error: function (xhr, textStatus, errorThrown) {
            console.log(errorThrown);
        }
    });

    return false;
}

function email() {
    $.ajax({
        url: BASE_URL + "/api/v1/email/",
        type: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        data: JSON.stringify({"email": $("#email").val()}),
        success: function (data, textStatus, xhr) {
            $("#email_response").show();

            if(data["result"].length==0){
                $("#email_response").html("<h3>Your email it's ok! Nothing found.</h3>");
            }else{
                var leaks = "";

                for (var i=0; i<data["result"].length; i++){
                    leaks += " " + data["result"][i] + ",";
                }

                $("#email_response").html("<h3>Your email is in the following leaks:"+leaks.slice(0, -1)+"</h3>");
            }
        },
        error: function (xhr, textStatus, errorThrown) {
            console.log(errorThrown);
        }
    });
    return false;
}