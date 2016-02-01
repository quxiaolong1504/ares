$(function(){
  "use strict";

  var user = new User();

  user.is_login(function(ret){
    console.info(ret);
  });

});

var User = (function(){
  "use strict";
  var api={}, internal={};

  api.is_login = function(callback){
    var url = "http://sms.snbway.com/api/auth/login/";
    $.ajax({
      type: 'GET',
      url : url,
      success: function(d,s){
        console.info('in is login');
        console.info(d);
        console.info(s);
        callback(d,s);
      }
    });
  };

  return api;
});