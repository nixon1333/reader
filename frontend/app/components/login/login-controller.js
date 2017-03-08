/**
 * Created by nixon on 05-Mar-17.
 */
function LoginController() {
    var that = this;
    that.foo = "Foo bars!";
    console.log(that); // should print out the controller object

    that.loginSubmit = function () {
        console.log("Just Hitted Submit");
        console.log(this.username);
        console.log(this.password);
    };


}

angular.module("Login")
    .controller("LoginController", [
        LoginController
    ]);