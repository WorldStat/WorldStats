

$(document).ready(function () {

    let valid1 = false;
    let valid2 = false;
    let valid3 = false;
    let valid4 = false;

    let regExpr1 = /^[a-zA-Z][a-zA-Z0-9_\-]{5,13}$/;  // for login
    let regExpr2 = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[_\-])[A-Za-z0-9_\-]{8,}$/;  // for password
    let regExpr3 = /^([a-z0-9_\-]+\.)*[a-z0-9_\-]+@[a-z0-9_\-]+(\.[a-z0-9_\-]+)*\.[a-z]{2,6}$/;  // for email

    $('#login').blur(function () {
        let _login = $(this).val();
        if (regExpr1.test(_login)) {
            // checking if login is available
            $.ajax({
                url: '/account/ajax_reg',
                data: 'login=' + _login,
                success: function(result) {
                    if (result.mess == 'login taken') {
                        $('#login_ico').attr('src', '../../static/img/cross.png');
                        $('#login_err').text('login taken');
                        valid1 = false;
                    } else {
                        $('#login_ico').attr('src', '../../static/img/ok.png');
                        $('#login_err').text('');
                        valid1 = true;
                    }
                }
            });
        } else {
            $('#login_ico').attr('src', '../img/cross.png');
            $('#login_err').text('Login must be 5-16 letters/numbers');
            valid1 = false;
        }
    });

    $('#pass1').blur(function () {
        let _pass1 = $(this).val();
        if (regExpr2.test(_pass1)) {
            $('#pass1_ico').attr('src', '../../static/img/ok.png');
            $('#pass1_err').text('');
            valid2 = true;
        } else {
            $('#pass1_ico').attr('src', '../../static/img/cross.png');
            $('#pass1_err').text('Password must be longer than 8 letters/numbers (At least one uppercase, lowercase letter, one number, one special symbol');
            valid2 = false;
        }
    });

    $('#pass2').blur(function () {
        let _pass1 = $('#pass1').val();
        let _pass2 = $('#pass2').val();
        if (_pass1 == _pass2) {
            $('#pass2_ico').attr('src', '../../static/img/ok.png');
            $('#pass2_err').text('');
            valid3 = true;
        } else {
            $('#pass2_ico').attr('src', '../../static/img/cross.png');
            $('#pass2_err').text('Passwords must match');
            valid3 = false;
        }
    });

    $('#email').blur(function () {
        let _email = $(this).val();
        if (regExpr3.test(_email)) {
            $('#email_ico').attr('src', '../../static/img/ok.png');
            $('#email_err').text('');
            valid4 = true;
        } else {
            $('#email_ico').attr('src', '../../static/img/cross.png');
            $('#email_err').text('Email like yourdomai@gmail.com');
            valid4 = false;
        }
    });

    $('#login').focus(function () {
        $('#login_ico').attr('src', '../../static/img/question.png');
        $('#login_err').text('');
    });

    $('#pass1').focus(function () {
        $('#pass1_ico').attr('src', '../../static/img/question.png');
        $('#pass1_err').text('');
    });

    $('#pass2').focus(function () {
        $('#pass2_ico').attr('src', '../../static/img/question.png');
        $('#pass2_err').text('');
    });

    $('#email').focus(function () {
        $('#email_ico').attr('src', '../../static/img/question.png');
        $('#email_err').text('');
    });

    $('#submit').click(function () {
        if (valid1 == true && valid2 == true && valid3 == true && valid4 == true) {
            $('#form1').attr('onsubmit', 'return true');
        } else {
            $('#form1').attr('onsubmit', 'return false');
            alert('Form contains incorrect data! \nSending of data is blocked!')
        }
    })

});


