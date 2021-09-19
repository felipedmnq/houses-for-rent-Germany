<p align="center">
  <img width="260" height="350" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Flag_map_of_Germany.svg/300px-Flag_map_of_Germany.svg.png">
</p>
<h1 align="center">Houses for Rent in Germany</h1>
<h3 align="center">https://rent-houses-germany.herokuapp.com/</h3>

   - This project aims to use web scraping to collect rental houses and apartments in major German cities for use in further analysis and studies.
 

   ## The Problem

   - In a few months I'll move to Germany, so, I need to rent a house to live in. In order to do that, I need to know how does work rent in Germany, how much I'll spend in average with rent itself, how does work with pets (I've a huge dog - Odin - and a little cat that I'll take with me), are pets allowed? Which size, location, and so on.

   Rent houses website: https://housinganywhere.com/

   ## The Solution

   - As solution tools, I planned to use Python's Beautiful Soup library to scrape the data from the rent houses website and than use other python libraryes to cleaning,          transform and analyse the scraped data.
    After that, I decided to use Streamlit library and build an app to deploy the work results on Heroku.

   ### Tools used in this project:

   <table>
     <tbody>
       <tr valign="top">
          <td width="25%" align="center">
            <span>Python</span><br><br>
            <img height="64px" src="https://cdn.svgporn.com/logos/python.svg">
          </td>
          <td width="25%" align="center">
            <span>BeautifulSoup</span><br><br>
            <img height="64px" src="https://sixfeetup.com/blog/an-introduction-to-beautifulsoup/@@images/27e8bf2a-5469-407e-b84d-5cf53b1b0bb6.png">
          </td>
          <td width="25%" align="center">
            <span>Pandas</span><br><br>
            <img height="64px" src="https://pandas.pydata.org/static/img/pandas.svg">
          </td>
          <td width="25%" align="center">
            <span>NumPy</span><br><br>
            <img height="64px" src="https://numpy.org/images/logos/numpy.svg">
          </td>
        </tr>
        <tr valign="top">
          <td width="25%" align="center">
            <span>Matplotlib</span><br><br>
            <img height="64px" src="https://matplotlib.org/_images/sphx_glr_logos2_001.png">
          </td>
          <td width="25%" align="center">
            <span>Seaborn</span><br><br>
            <img height="64px" src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg">
          </td>
          <td width="25%" align="center">
            <span>Plotly</span><br><br>
            <img height="64px" src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Plotly_logo_for_digital_final_%286%29.png">
          </td>
          <td width="25%" align="center">
            <span>Json</span><br><br>
            <img height="64px" src="https://pngimage.net/wp-content/uploads/2018/06/json-png-7.png">
          </td>
        <tr valign="top">
          <td width="25%" align="center">
            <span>Folium</span><br><br>
            <img height="64px" src="https://data-science-and-design.readthedocs.io/en/latest/_images/folium.png">
          </td>
          <td width="25%" align="center">
            <span>FPDF</span><br><br>
            <img height="64px" src="https://warehouse-camo.ingress.cmh1.psfhosted.org/240e7de884ccbd0d1f70bf097b4aa7e84bd01b2d/68747470733a2f2f7079667064662e6769746875622e696f2f66706466322f66706466322d6c6f676f2e706e67">
          </td>
          <td width="25%" align="center">
            <span>Heroku</span><br><br>
            <img height="64px" src="https://blog.4linux.com.br/wp-content/uploads/2018/01/Heroku.png">
          </td>
          <td width="25%" align="center">
            <span>Streamlit</span><br><br>
            <img height="64px" src="https://assets.website-files.com/5dc3b47ddc6c0c2a1af74ad0/5e18182ad27bcfbb9dff263a_RGB_Logo_Horizontal_Color_Light_Bg-p-1080.png">
          </td>
        <tr valign="top">
          <td width="25%" align="center">
            <span>RegEx</span><br><br>
            <img height="64px" src="https://repository-images.githubusercontent.com/186091864/e96c1a80-7a27-11e9-8232-2b21d5d861d3">
          </td>
          <td width="25%" align="center">
            <span>IPython</span><br><br>
            <img height="64px" src="https://miro.medium.com/max/721/1*T_nQFZEcSVoZtiCf20B2rA.png">
          </td>
          <td width="25%" align="center">
            <span>base64</span><br><br>
            <img height="64px" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCxYwe33cDiCfAyZZpbmgu46_BQoWEQ6YK2J0WSoT5sZU4YuCB6-oM72P-jg4yMPBSqxk&usqp=CAU">
          </td>
          <td width="25%" align="center">
            <span>Requests</span><br><br>
            <img height="64px" src="https://static.tildacdn.com/tild3135-6235-4366-b435-656633353166/a21_Smartiqa_python_.png">
          </td>
        </tr>
      </tbody>
    </table>
    
   ## Data Collection, Cleanning and Transformation
    
   - In order to scrape the data from "housinganywhere" website, I used the BeautifulSoup python library and wrote a python code that collects several infos about the houses offers, like ID, address, montly rent value, deposit value, size, location coordinates and, more important for me, if pets are allowed. 
    BeautifulSoup is a very nice python library, is easy to implement and with a basic knowledge of html, is possible to collect all kinds of information from websites. i had lots of fun using BS and have learned a lot, mostly about html.
    
   - With all the data about the houses and using the coordinates from each house offer, I called Foursquare API to get places of interest in a 300 meters radius of each house. With this infos i can know wath has around the houses, like restaurants, parks, public transport, movies an so on. 
    
   - After the web scraping, I've done the data cleaning and transformation, that took me many hours of work and bring me lots of knowledge about data cleaning. In this fase of the project, the most nice think that I learned was how to use RegEx to extract infos from strings, RegEx is very hard to learn, but is a very powerfull tool.
    
   ## Exploratory Data Analysis
    
   - Now, with all the data I need, and after the cleaning, is time to analyse all this data. Using Pandas, Seaborn, Matplotlib, Folium and other libraries, I done a complete EDA in orther to get insigths aboult how works houses rent in Germany and get sone valious infos related to houses rent.

   ### Decriptive Analysis
    
   - It was collected 1668 houses offers from Berlin, Munich, Dusseldorf, Cologne, Dortmund, Frankfurt, Nuremberg, Stuttgart, Hamburg, Hanover and Leipzig. The main caracteristics from the Germany Rent Houses dataset is disposed in the following table: 
    
   |                   |   count |      mean |       std |   min |       25% |       50% |      75% |      max |
   |:------------------|--------:|----------:|----------:|------:|----------:|----------:|---------:|---------:|
   | Size - m²         |    1668 |   51.3543 |   25.4503 |    15 |   33      |   47      |   63     |  220     |
   | Montly Rent - €   |    1668 | 1588.39   |  787.581  |   350 | 1057.5    | 1400      | 1860     | 6490     |
   | Deposit Value - € |    1668 | 1614.59   | 1283.75   |     0 |  690      | 1500      | 2250     | 9990     |
   | m2 Value - €      |    1668 |   33.5445 |   14.37   |     5 |   24.4186 |   30.4527 |   39.375 |  143.333 |

    
   #### The next graphs shows us distribution of each feature per city:
    
   ##### Hauses offers per city.
   ![rent_houses_per_city](https://user-images.githubusercontent.com/71295866/120832524-246e1780-c537-11eb-8fb9-f902c929a5cc.png)
    
   ##### Monthly rent price distribution per city.
   ![montly_rent_per_city](https://user-images.githubusercontent.com/71295866/120833002-a3fbe680-c537-11eb-99bd-aaa30d037109.png)
   ![boxplot_rent_distrition_per_city](https://user-images.githubusercontent.com/71295866/120833383-1b317a80-c538-11eb-9072-af3d4db3abcc.png)
    
   ##### Pets allowance policy distribution.
   ![count_pets_permission](https://user-images.githubusercontent.com/71295866/120833721-8418f280-c538-11eb-969d-3c1c657b6c88.png)

   - How we can see from the graph, almost half of the houses offers specified that pets are not allowed, so, I think that maybe can be a little hard to find a place who accepts my dog and my cat, but it is ok. I'm sure that I'll find some place. :smiley_cat: :service_dog:

   ## Streamlit App Creation.
    
   - In order to be able to see the results from my rent houses data collection, I build an app using the Streamlit library. In this app i inserted filters to select one or more cities, a range of rent prices, if pets are or aren't allowed and than I used Plotly librarie to plot some graphs with the filtered dataset.
    
   ##### Filters
   <p align="center">
       <img width="260" height="350" src="https://i.gyazo.com/366b7a175b95c3205e35ea7cd7e0e289.gif">
   </p>

   -  After that I used Folium librarie to display a map eith the localization of each house offer, filtered accordingli with the user preferences, showing the address, the rent price and if pets are allowed or not.
    
   ##### Map
   <p align="center">
       <img width="260" height="350" src="https://i.gyazo.com/df6c743c1519f759f7564b7430f612c3.gif">
   </p>

   - Than, after the user have selected all the preferences, he can download a CSV file with the filtered dataset and also a full PDF report, created using the FPDF library.
    
   ##### Files Download
   <p align="center">
       <img width="260" height="350" src="https://i.gyazo.com/9f7feb73410bdfca9a4e656c49dfee5f.gif">
   </p>
    
   ## Heroku Deploy
    
   - To show my work to everyone who is interested, I've deployed the streamlit app into Heroku, and now is just click the link below and use the app as you're pleased.
    
   [Rent Houses in Germany App](https://rent-houses-germany.herokuapp.com/)
    
   ## Conclusion
   - This was my first "end-to-end" project and was really fun to do it.  Data Science is for me a hobby for now, I only have a few free hours a day to dedicate to my projects so it was challenging. I had several issues that I struggle hard to figure out, sometimes when I managed to solve a problem, it was very nice, the feeling was wonderful, then another problem came up, and so on, the project was progressing.
    
   - With this project I could learn a lot about web screaping, html, several python libraries and python itself. I learned how to build a full app and how to deploy it.
    But most importantly, I'm able to solve a problem with my own hands. As a great teacher I follow says: "the tools used don't matter, the important thing is to solve the        problem!"

   ## References
    
   * https://housinganywhere.com/
   * https://docs.streamlit.io/en/stable/
   * https://github.com/isellsoap/deutschlandGeoJSON
   * https://python-visualization.github.io/folium/    
   * https://developer.foursquare.com/docs/
   * https://pandas.pydata.org/docs/
   * https://seaborn.pydata.org/
   * https://matplotlib.org/stable/contents.html
   * https://www.crummy.com/software/BeautifulSoup/bs4/doc/
   * https://www.regextester.com/
   * https://devcenter.heroku.com/categories/reference
       
