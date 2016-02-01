$(function(){
  "use strict";

  var user = new User();

  if(user.is_login()){
    console.info(true);
  }
  else{
    user.login('quxl', 'quxiaolong');
  }

  var sms = new Sms();
  console.info(sms.get_sms());


});

var User = (function(){
  "use strict";
  var api={}, internal={};

  api.is_login = function(callback){
    var url = "http://sms.snbway.com/api/sms/";
    var ret = false;
    $.ajax({
      type: 'GET',
      url : url,
      async: false,
      success: function(d,s){
        ret = true;
      },
      error: function(d, s){
        if(d.status==401){
          ret = false;
        }
      }
    });
    return ret
  };

  api.login = function(username, password){
    var url = "http://sms.snbway.com/api/auth/login/";
    var ret = false;
    var csrftoken = internal.get_scrftoken();
    console.info(csrftoken);
    $.ajax({
      type: 'POST',
      url : url,
      async: false,
      data: {username: username, password: password, csrfmiddlewaretoken: 'oxUZGnRF33pKoEo77os3KKuZuEuFAyFK'},
      xhrFields: {
        withCredentials: true
      },
      success: function(d,s){
        console.info(d,s);
      },
      error: function(d, s){
        if(d.status==401){
          ret = false;
        }
      }
    });
    return ret
  };


  internal.get_scrftoken = function(){
    if(typeof internal.csrfmiddlewaretoken != "undefined"){
      return internal.csrfmiddlewaretoken;
    }
    var url = "http://sms.snbway.com/api/auth/login/";
    var ret = "";
    $.ajax({
      type: "GET",
      url: url,
      async: false,
      success : function(d,s,xhr){
        var reg = /csrfmiddlewaretoken.*\/>/g
        var tmp_str = reg.exec(d)[0];
        reg = /value='.*'/g;
        tmp_str = reg.exec(tmp_str)[0];
        tmp_str = tmp_str.substr(7)
        ret = tmp_str.substr(0, tmp_str.length-1)
      }
    });
    internal.csrfmiddlewaretoken = ret;
    return ret;
  };

  return api;
});


var Sms = (function(){
  "use strict";
  var api={};

  api.get_sms = function(){
    var url = "http://sms.snbway.com/api/sms/";
    var ret = [];
    $.ajax({
      type: 'GET',
      url : url,
      async: true,
      xhrFields: {
        withCredentials: true
      },
      success: function(d,s){
        ret = d
        console.info(d)
        console.info(s)
      },
      error: function(d, s){
        if(d.status==401){
          ret = false;
        }
      }
    });
    return ret
  };


  return api;
});