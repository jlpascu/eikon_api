# eikon_api
In this repository you can find fast tips that can help you out when you are using Eikon API for Python

#### We will be using serveral date formats. You can find all date formats accepted by Eikon Api on the following screan shot
![Screenshot 2021-12-18 at 20 14 49](https://user-images.githubusercontent.com/69301150/146675427-e1d89493-0bc8-4118-a5a0-533388163317.png)

When running a back testing on an algorithm that trades trying to beat an equity index, you must make sure that your historical data considers the index constituents on the back testing starting date and you keep updating that information on a yearly basis. Otherwise, if you use current equity index constituents your algorithm will be affected by survivorship bias. See Update download_equity_index_constituents.py for suggested code.  
