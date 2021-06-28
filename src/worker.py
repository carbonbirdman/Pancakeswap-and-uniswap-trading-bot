# Worker class, ideally spawn a few of these right?
w33 = Web3()
cg = CoinGeckoAPI()

# Holds information about a coin and what we want to do with it
class Coin(object):
    def __init__(self,param_list):
        self.data = param_list

class Worker(Object):
    # change these to some sort of signal class
    sig_step = "step"
    sig_done = "done"
    sig_msg = "msg"

    def __init__(self, id):
        super().__init__()
        self.__id = id
        self.__abort = False
        print("Initialising worker")

    def work(self):
        maxgwei = int(configfile.maxgwei)
        maxgweinumber = int(configfile.maxgweinumber)
        diffdeposit = float(configfile.diffdeposit)
        diffdepositaddress = str(configfile.diffdepositaddress)
        speed = str(configfile.speed)
        max_slippage = float(configfile.max_slippage)
        incaseofbuyinghowmuch = int(configfile.incaseofbuyinghowmuch)
        ethtokeep = int(configfile.ethtokeep)
        timesleepaftertrade = int(configfile.secondscheckingprice_2)
        timesleep = int(configfile.secondscheckingprice)
        infura_url = str(configfile.infuraurl)
        infuraurl = infura_url
        tokentokennumerator = float(configfile.tokentokennumerator)
        mcotoseeassell = float(configfile.mcotoseeassell)
        debugmode = int(configfile.debugmode)

        coin1 = Coin([1,
                      str(configfile.token1ethaddress),
                      float(configfile.token1high),
                      float(configfile.token1low),
                      float(configfile.activatetoken1),
                      float(configfile.token1stoploss),
                      float(configfile.stoplosstoken1),
                      float(configfile.tradewithERCtoken1),
                      float(configfile.tradewithETHtoken1),
                      '0',
                      str(configfile.token1name),
                      int(configfile.token1decimals)])

        coin2 = Coin([2,
                      str(configfile.token2ethaddress),
                      float(configfile.token2high),
                      float(configfile.token2low),
                      float(configfile.activatetoken2),
                      float(configfile.token2stoploss),
                      float(configfile.stoplosstoken2),
                      float(configfile.tradewithERCtoken2),
                      float(configfile.tradewithETHtoken2),
                      '0',
                      str(configfile.token2name),
                      int(configfile.token2decimals)])

        while self.__abort != True:
            print("Doing work")
            # Read config values
            # for token_number, eth_address,
            # high, low, activate, stoploss_value, stoploss_activate,
            # trade_with_ERC, trade_with_ETH, fast_token
            # its now: for token_number,eth_address
            # high,low,activate,stoploss_value,stoploss_activate
            # trade_with_ERC,trade_with_ETH,fast_token
            # small_case_name,decimals in all_token_information:
            for coin in [coin1,coin2]:
                token_number, eth_address, high, low, activate, stoploss_value, stoploss_activate, \
                trade_with_ERC, trade_with_ETH, fast_token, small_case_name, decimals = coin.data

                if (high < low):
                    print('Stop the script, a tokenlow is higher than its tokenhigh')
                    count = 0
                if (stoploss_value > high):
                    print('Stop the script, a stoploss is higher than the tokenhigh')
                    count = 0
                if (ethtokeep > mcotoseeassell):
                    print('The buy/sell boundary is lower than the $ to keep in BNB after trade')
                    count = 0
            my_address = str(configfile.my_address)
            my_pk = str(configfile.my_pk)

            pk = my_pk
            if configfile.maincoinoption == 'BNB':
                ethaddress = "0x0000000000000000000000000000000000000000"
                maindecimals = 18
            if configfile.maincoinoption == 'DAI':
                ethaddress = "0x1af3f329e8be154074d8769d1ffa4ee058b1dbc3"
                maindecimals = 18
            if configfile.maincoinoption == 'BUSD':
                ethaddress = "0xe9e7cea3dedca5984780bafc599bd69add087d56"
                maindecimals = 18
            if configfile.maincoinoption == 'USDC':
                ethaddress = "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d"
                maindecimals = 18
            if configfile.maincoinoption == 'wBTC':
                ethaddress = "0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c"
                maindecimals = 18
            if configfile.maincoinoption == 'ETH':
                ethaddress = "0x2170ed0880ac9a755fd29b2688956bd959f933f8"
                maindecimals = 18
            maincoinname = configfile.maincoinoption
            maincoinoption = ethaddress

            if 'step' not in locals():
                step = 1
            else:
                step = 1
            #self.sig_step.emit(self.__id, 'step ' + str(step))
            if self.__abort == True:
                print('Worker #{} aborting work at step {}'.format(self.__id, step))
            totaldollars = 1

            # END WHILE LOOP
            # END WORK FUNCTION
