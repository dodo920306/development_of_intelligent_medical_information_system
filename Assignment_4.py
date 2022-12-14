def chat(s : str) -> str:
    if '幫我搜尋附近的餐廳':
        return '好的，結果如下：'
    elif '我有個10~20人的聚會要在下禮拜五晚上舉行，請問離我現在位置最近的建議地點為何':
        return '好的，結果如下：...需要幫您撥號訂位嗎?'
    elif '最近的，有營業至晚上10點的咖啡廳在哪':
        return '為您推薦：'
    elif '台南評價最高的土產店為?':
        return '台南評價最高的土產店為：'
    elif '成大附近價格100以下，14點有營業的餐廳，評價最高為?':
        return '應為：'
    elif '早餐吃什麼':
        return '推薦吃：'
    elif '午餐吃什麼':
        return '推薦吃：'
    elif '晚餐吃什麼':
        return '推薦吃：'
    elif '幫我規劃在一日在台中逢甲商圈的午晚餐':
        return '好的，結果如下：'
    elif '幫我找最近的麥當勞':
        return '好的，最近的麥當勞在：'
    elif '幫我找附近最便宜的成衣店':
        return '好的，結果如下：'
    elif '我想訂製一套西裝，附近目前有營業的，CP值最高的店家為?':
        return '好的，結果如下：...需要幫您撥號預約嗎'
    elif '我想找皮製飾品，如皮帶和皮夾，附近有這種店家嗎?':
        return '好的，結果如下：'
    elif '我想找牛仔衣物，附近有這種店家嗎?':
        return '好的，結果如下：'
    elif '我想找丹寧衣物，附近有這種商家嗎?':
        return '好的，結果如下：'
    elif '我現在人在台北101，可以幫我找101商圈中CP值最高的幾家衣服店嗎':
        return '好的，結果如下：'
    elif '我知道Cosplayer不自製套裝是有違職業道德的，但我下禮拜四真的很需要戲服，可以幫我找附近的店家嗎?':
        return '好的，結果如下：'
    elif '我想要一只石英錶，幫我找附近的鐘錶店':
        return '好的，結果如下：'
    elif '我想找便宜的項鍊飾品':
        return '好的，結果如下：'
    elif '我想找韓系襯衫':
        return '好的，結果如下：'
    elif '幫我整理7日內在成大租屋敖屋敖屋中刊登的租屋資訊':
        return '好的，整理如下：'
    elif '幫我整理房東爭議相關的法條':
        return '好的，結果如下：'
    elif '幫我找北車附近的青旅':
        return '好的，結果如下：'
    elif '幫我找台北便宜的青旅':
        return '好的，結果如下：'
    elif '幫我找台南便宜的青旅':
        return '好的，結果如下：'
    elif '幫我預約阿里山上下禮拜三晚上的四人房':
        return '好的，推薦旅館如下：...如果適合便幫您撥號'
    elif '幫我預約義大的旅館，下下禮拜六晚上':
        return '好的，跳轉至付款頁面'
    elif '幫我預約綠島的旅館，下下禮拜四五六晚上':
        return '好的，跳轉至付款頁面'
    elif '幫我找台中離火車站近的便宜的青旅':
        return '好的，結果如下：'
    elif '幫我整理中壢的租屋刊登資訊':
        return '好的，整理如下：'
    elif '幫我安排下禮拜五晚上的高鐵，從台南到台北':
        return '好的，跳轉至預約頁面'
    elif '幫我安排綠島三日遊，下禮拜五到日':
        return '好的，安排如下：'
    elif '幫我安排下下禮拜一早上的高鐵，從台北到台南':
        return '好的，跳轉至預約頁面'
    elif '幫我安排桃機到東京的航班，5/5早上，靠窗，一人':
        return '好的，跳轉至預約頁面'
    elif '幫我尋找附近的出租機車店家':
        return '好的，結果如下：'
    elif '幫我安排下禮拜五晚上的客運，從高雄到桃園':
        return '好的，跳轉至預約頁面'
    elif '幫我安排下禮拜五晚上的台鐵，從高雄到台中':
        return '好的，跳轉至預約頁面'
    elif '我現在在美麗島站，請問透過捷運怎麼到歌劇院':
        return '好的，結果如下：'
    elif '幫我搜尋台北車站地圖，我迷路了':
        return '好的，結果如下：'
    elif '幫我搜尋北捷路網圖':
        return '好的，結果如下：'
    else:
        return '很抱歉，我無法回答。'


if __name__=='__main__':
    x = input('你有什麼問題?')
    print(chat(x))