require(["dojo/parser",
         "dojo/ready", 
         "dojo/domReady!",
         "dijit/Menu",
         "dijit/MenuItem",
         "dijit/MenuBar",
         "dijit/MenuBarItem",
         "dijit/PopupMenuBarItem", 
         "dijit/form/TextBox", 
         "dijit/form/Button"],
     function(parser, ready){
    	    ready(function(){
    	        parser.parse();
    	    });
    	});