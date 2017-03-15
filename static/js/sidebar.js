/**
 * Created by Administrator on 2016/7/2.lijizhixing
 */
(function(){
    var Sidebar=function(eId,closeBarId){
        this.state='opened';
        this.e1=document.getElementById(eId||'sidebar');
        this.closeBarE1=document.getElementById(closeBarId||'');
        var self=this;
        this.el.addEventListener('click',function(event){
            if(event.target!==self.el)
            {self.triggerSwitch();}
        });
    };
    Sidebar.prototype.close=function(){
        alert("guanbi");
        this.state="closed";
    };
    Sidebar.prototype.open=function(){
        alert("dakai");
        this.state="opened";
    };
    Sidebar.prototype.triggerSwitch=function(){
        if(this.state==='opened')
        {this.close();}
        else
        {this.open();}
    };
    var sidebar=new Sidebar();
})();