$(document).ready(function() {
aObj = document.getElementById('nav').getElementsByTagName('a');
		listObj = document.getElementById('nav').getElementsByTagName('li');
	if(location.pathname != "/catalog/") {
		for(i=1;i<aObj.length;i++) {
		if(document.location.href.indexOf(aObj[i].href)>=0) {
		  listObj[i].className='navhome';
		}
		else if(location.pathname == "/accounts/login/"){listObj[5].className='navhome';}
	  }
	}
	else{listObj[0].className='navhome';}
	if(location.pathname == "/"){
		listObj[0].className='navhome';
	}







});

