var mainVM = new Vue({
    el: 'body',
    data: {
        shopes:[
            {
                shopname:'未查询',
                dsr:'未查询',
                service:'未查询',
                ship:'未查询'
            }
        ]
    },
    methods:{
        query:function(){
            var _self = this,keyword = $('input[name="shopname"]').val();
            $.post('/query',{"shopname":keyword},function (data) {
                if(data.code == 0){
                    _self.shopes = [];

                    for(var k in data.rows){
                        var thisdata = JSON.parse(data.rows[k]);
                        _self.shopes.push({
                            shopname:thisdata.shopname,
                            dsr:thisdata.dsr,
                            service:thisdata.service,
                            ship:thisdata.ship
                        })
                    }
                }else{
                    alert('查询出错，错误信息：'+data.msg);
                }
            },"json");
        }
    }
});