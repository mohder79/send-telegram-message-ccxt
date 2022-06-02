import ccxt
import api_confing_my_bybit as ac
import time
import requests

# -----------------------------------------------------------------------------
TOKEN = '***********'  # telegram token
CHAT_ID = '**************'  # telegram chat id
SEND_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
exchange = ccxt.bybit({
    'enableRateLimit': True,
    'apiKey': ac.API_KEY,
    'secret': ac.SECRET_KEY,
    'password': ac.PASSWORD,
})
exchange.options['adjustForTimeDifference'] = True
exchange.load_markets()
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
amount = 0.001
price = None
symbol = 'BTC/USDT:USDT'
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
long_sl_tp = {
    'stop_loss': 20000,  # stop price
    'type': 'stopMarket',
    'take_profit': 50000,  # profit price
}  # long take profit & stop loss price
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
short_sl_tp = {
    'stop_loss': 50000,  # stop price
    'type': 'stopMarket',
    'take_profit': 20000,  # profit price
}  # short take profit & stop loss price
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
reduce_only = {
    'reduce_only': True
}  # reduce_only params for close open position
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
parambuy = {
    'side': 'buy',

}  # positions buy side params
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
paramsell = {
    'side': 'sell',

}  # positions sell side params
# -----------------------------------------------------------------------------

run = True

while run == True:
    print('bot is working')
    time.sleep(2)
# position side buy -----------------------------------------------------------------------------
    open_position = exchange.create_order(
        symbol, 'market', 'buy', amount, price, params=long_sl_tp)
    time.sleep(2)
    print('bot open buy position')
    positions = exchange.fetch_positions(symbols=symbol, params=parambuy)
    # position entry price
    pos_entry_price = str(positions[0]['info']['entry_price'])
    # position liq price
    pos_liq_price = str(positions[0]['info']['liq_price'])
    pos_leverage = str(positions[0]['leverage'])  # position leverage
    pos_size = str(positions[0]['info']['size'])  # position size
    pos_side = str(positions[0]['info']['side'])  # position side
    # position stop loss
    pos_stop_loss = str(positions[0]['info']['stop_loss'])
    # position take profit
    pos_take_profit = str(positions[0]['info']['take_profit'])
    mysymbol = str(positions[0]['info']['symbol'])  # position symbol
    requests.post(SEND_URL, json={
                  'chat_id': CHAT_ID, 'text': u'🤖' + f' open position\n symbol:{mysymbol} \n side:{pos_side} \n size:{pos_size} \n entry_price:{pos_entry_price} \n liq_price {pos_liq_price} \n stop loss: {pos_stop_loss}  \n take profit: {pos_take_profit} \n leverage: {pos_leverage}'})
    time.sleep(20)

    positions = exchange.fetch_positions(symbols=symbol, params=parambuy)
    # position entry price
    pos_entry_price = str(positions[0]['info']['entry_price'])
    # position liq price
    pos_liq_price = str(positions[0]['info']['liq_price'])
    pos_leverage = str(positions[0]['leverage'])  # position leverage
    pos_size = str(positions[0]['info']['size'])  # position size
    pos_side = str(positions[0]['info']['side'])  # position side
    # position stop loss
    pos_stop_loss = str(positions[0]['info']['stop_loss'])
    # position take profit
    pos_take_profit = str(positions[0]['info']['take_profit'])
    mysymbol = str(positions[0]['info']['symbol'])  # position symbol
    # position unrealised pnl
    pos_unrealised_pnl = str(positions[0]['info']['unrealised_pnl'])
    requests.post(SEND_URL, json={
                  'chat_id': CHAT_ID, 'text': u'🤖' + f' open position\n symbol:{mysymbol} \n side:{pos_side} \n size:{pos_size} \n entry_price:{pos_entry_price} \n liq_price {pos_liq_price} \n stop loss: {pos_stop_loss}  \n take profit: {pos_take_profit} \n leverage: {pos_leverage} \n unrealised pnl:{pos_unrealised_pnl}'})
    time.sleep(20)
    close_position = exchange.create_order(
        symbol, 'market', 'sell', amount, price, params=reduce_only)
    time.sleep(2)
    print('bot close buy position')
    requests.post(SEND_URL, json={
                  'chat_id': CHAT_ID, 'text': u'🤖' + ' close your position'})
 # position side buy -----------------------------------------------------------------------------
    time.sleep(20)
 # position side sell -----------------------------------------------------------------------------
    order = exchange.create_order(
        symbol, 'market', 'sell', amount, price, params=short_sl_tp)
    time.sleep(2)
    print('bot open sell position')

    positions = exchange.fetch_positions(symbols=symbol, params=paramsell)
    # position entry price
    pos_entry_price = str(positions[0]['info']['entry_price'])
    # position liq price
    pos_liq_price = str(positions[0]['info']['liq_price'])
    pos_leverage = str(positions[0]['leverage'])  # position leverage
    pos_size = str(positions[0]['info']['size'])  # position size
    pos_side = str(positions[0]['info']['side'])  # position side
    # position stop loss
    pos_stop_loss = str(positions[0]['info']['stop_loss'])
    # position take profit
    pos_take_profit = str(positions[0]['info']['take_profit'])
    mysymbol = str(positions[0]['info']['symbol'])  # position symbol
    requests.post(SEND_URL, json={
                  'chat_id': CHAT_ID, 'text': u'🤖' + f' open position\n symbol:{mysymbol} \n side:{pos_side} \n size:{pos_size} \n entry_price:{pos_entry_price} \n liq_price {pos_liq_price} \n stop loss: {pos_stop_loss}  \n take profit: {pos_take_profit} \n leverage: {pos_leverage}'})
    time.sleep(20)
    positions = exchange.fetch_positions(symbols=symbol, params=paramsell)
    # position entry price
    pos_entry_price = str(positions[0]['info']['entry_price'])
    # position liq price
    pos_liq_price = str(positions[0]['info']['liq_price'])
    pos_leverage = str(positions[0]['leverage'])  # position leverage
    pos_size = str(positions[0]['info']['size'])  # position size
    pos_side = str(positions[0]['info']['side'])  # position side
    # position stop loss
    pos_stop_loss = str(positions[0]['info']['stop_loss'])
    # position take profit
    pos_take_profit = str(positions[0]['info']['take_profit'])
    mysymbol = str(positions[0]['info']['symbol'])  # position symbol
    # position unrealised pnl
    pos_unrealised_pnl = str(positions[0]['info']['unrealised_pnl'])
    requests.post(SEND_URL, json={
                  'chat_id': CHAT_ID, 'text': u'🤖' + f' open position\n symbol:{mysymbol} \n side:{pos_side} \n size:{pos_size} \n entry_price:{pos_entry_price} \n liq_price {pos_liq_price} \n stop loss: {pos_stop_loss}  \n take profit: {pos_take_profit} \n leverage: {pos_leverage} \n unrealised pnl:{pos_unrealised_pnl}'})
    time.sleep(20)
    close_position = exchange.create_order(
        symbol, 'market', 'buy', amount, price, params=reduce_only)
    time.sleep(2)
    print('bot close sell position')

    requests.post(SEND_URL, json={
                  'chat_id': CHAT_ID, 'text': u'🤖' + ' close your position'})

    time.sleep(300)
