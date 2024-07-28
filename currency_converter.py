def currency_convertor():
    print('This will only convert the currency of pakistan into usd')
    while True:
        User=int(input('Enter please : '))
        pkr = 280
        #  As we know that one usd is equal to 280 pkr 
        print('You enterd {}'.format(User))
        result = pkr*User
        print('The {} usd is equal to {}pkr '.format(User,result))
        
    else:
        print('SOrry this is invalid ')
currency_convertor()