# Coffee Machine Simulator

## Description

This is a simple coffee machine simulator. User can pick between 3 drinks. Every drink has 
its own resources needed and its cost. Machine is able to give the charge. 
Typing 'report' enables to check current state of resources.
Typing 'off' turns off the device

## Example Output

```

              _..,----,.._
            .-;'-.,____,.-';
           (( |            |
            `))            ;
             ` \          /
            .-' `,.____.,' '-.
           (     '------'     )
            `-=..________..--'
        
What would you like? (espresso/latte/cappuccino) report
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0.0
```
```

              _..,----,.._
            .-;'-.,____,.-';
           (( |            |
            `))            ;
             ` \          /
            .-' `,.____.,' '-.
           (     '------'     )
            `-=..________..--'
        
What would you like? (espresso/latte/cappuccino)latte
Please insert coins.
How many quarters?: 10
How many dimes?: 4
How many nickles?: 2
How many pennies?: 0
Your charge: $1.5
Here is your latte! Enjoy
```

## TO DO
- Exception handling
- Add more Drinks
- More complex Report
