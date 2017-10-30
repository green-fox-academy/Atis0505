const Panama = {
    cash: 0,
    name: 'Panama',
    tax: '1%',
    deposit: function(amt) {
        this.cash += amt;
        console.log("Panama got "+amt);
    }
}

const Cyprus = {
    cash: 0,
    name: 'Cyprus',
    tax: '5%',
    deposit: function(amt) {
        this.cash += amt;
        console.log("Cyprus got "+amt);
    }
}

const Shuffler = {
    cash: 10000,
    pick: function() {
        if(Panama.cash > Cyprus.cash){
            Cyprus.deposit(1000)
        }else{
            Panama.deposit(1000)
        }
    }
}

Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000
Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000

console.log( Panama.cash ) // 2000 
console.log( Cyprus.cash ) // 2000 