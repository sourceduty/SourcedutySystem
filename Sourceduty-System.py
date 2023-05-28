#Sourceduty System V1.2
#Copyright (c) 2023, Sourceduty
#This software is free and open-source; anyone can redistribute it and/or modify it.

from tkinter import Tk, Menu
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image  
import subprocess
import random



# window root
root = Tk()
root.geometry('1000x500')
root.title('Sourceduty System')

# canvas object
canvas= Canvas(root, width= 1920, height= 1080, bg="black")

# text in Canvas
canvas.create_text(500, 120, text="""
   _____                              _       _            _____            _                 
  / ____|                            | |     | |          / ____|          | |                
 | (___   ___  _   _ _ __ ___ ___  __| |_   _| |_ _   _  | (___  _   _  ___| |_ ___ _ __ ___  
  \___ \ / _ \| | | | '__/ __/ _ \/ _` | | | | __| | | |  \___ \| | | |/ __| __/ _ \ '_ ` _ \ 
  ____) | (_) | |_| | | | (_|  __/ (_| | |_| | |_| |_| |  ____) | |_| |\__ \ ||  __/ | | | | |
 |_____/ \___/ \__,_|_|  \___\___|\__,_|\__,_|\__|\__, | |_____/ \__, ||___/\__\___|_| |_| |_|
                                                   __/ |          __/ |                      
           Copyright (c) 2023, Sourceduty         |___/          |___/     Made in Canada                  
""", fill="white", font=('Courier', 10))
canvas.pack()

# menubar
menubar = Menu(root)
root.config(menu=menubar)

# Design menu
design_menu = Menu(
    menubar,
    tearoff=0
)

# Design menu About item Child window
def my_child_main():
    my_w_child_main=Toplevel(root)  
    my_w_child_main.geometry("1000x500")  
    my_w_child_main.title("About")
    my_w_child_main.configure(bg='black')  
    
    canvas= Canvas(my_w_child_main, width= 1920, height= 1080, bg="black")

    # text in Canvas
    canvas.create_text(455, 100, text="""
Sourceduty is a design company created in 2022. This business is focused on industrial design, 
architecture, graphic design and 3D models. Sourceduty utilizes any medium, material and 
manufacturing process required to create new things.

Sourceduty System software is free and open-source; anyone can redistribute it and/or modify it.
    """, fill="white", font=('Courier', 10))
    canvas.pack()   
    
design_menu.add_command(label="About", command=lambda:my_child_main())

# Design menu Help item Child window
def my_child_help1():
    my_w_child_help1=Toplevel(root) 
    my_w_child_help1.geometry("1000x500")  
    my_w_child_help1.title("Help")
    my_w_child_help1.configure(bg='black')
    
    canvas= Canvas(my_w_child_help1, width= 1920, height= 1080, bg="black")

    # text in Canvas
    canvas.create_text(200, 75, text="""
Contact: sourceduty@gmail.com 
Website: sourceduty.com
    """, fill="white", font=('Courier', 10))
    canvas.pack()    
    
design_menu.add_command(label="Help", command=lambda:my_child_help1())

# Design label in menubar
menubar.add_cascade(
    label="Design",
    menu=design_menu,
    underline=0
)
# Log menu
log_menu = Menu(
    menubar,
    tearoff=0
)

# Games menu
game_menu = Menu(
    menubar,
    tearoff=0
)

# Games label in menubar
menubar.add_cascade(
    label="Games",
    menu=game_menu,
    underline=0
)

# Games menu item Sky Tetris
game_menu.add_command(label='Sky Tetris', command=lambda:run_program1())

# Run SkyTetris.py program 
def run_program1():
    subprocess.call(["python", "Sky Tetris.py"])

# Games menu item Ocean Invaders
game_menu.add_command(label='Ocean Invaders', command=lambda:run_program2())

# Run OceanInvaders.py program 
def run_program2():
    subprocess.call(["Ocean-Invaders.exe"])

# Games menu item 
game_menu.add_command(label='Tic Tac Toe', command=lambda:run_program3())

# Run any .py program 
def run_program3():
    subprocess.call(["python", "Tic Tac Toe.py"])

# Games menu About item Child Window
def my_w_child_game_about():
    my_w_child_game_about=Toplevel(root)  
    my_w_child_game_about.geometry("1000x500")  
    my_w_child_game_about.title("About")
    my_w_child_game_about.configure(bg='black')  
    
    canvas= Canvas(my_w_child_game_about, width= 1920, height= 1080, bg="black")

    # text in Canvas
    canvas.create_text(455, 100, text="""
Sourceduty is a design company created in 2022. This business is focused on industrial design, 
architecture, graphic design and 3D models. Sourceduty utilizes any medium, material and 
manufacturing process required to create new things.
    """, fill="white", font=('Courier', 10))
    canvas.pack()   
    
game_menu.add_command(label="About", command=lambda:my_w_child_game_about())

# Apps menu
apps_menu = Menu(
    menubar,
    tearoff=0
)

# Apps label in menubar
menubar.add_cascade(
    label="Apps",
    menu=apps_menu,
    underline=0
)

# Random location App
#Destinations
places = "Athabasca, Alberta","Banff, Alberta","Barrhead, Alberta","Bashaw, Alberta","Bassano, Alberta","Beaverlodge, Alberta","Bentley, Alberta","Blackfalds, Alberta","Bon Accord, Alberta","Bonnyville, Alberta","Bow Island, Alberta","Bowden, Alberta","Bruderheim, Alberta","Calmar, Alberta","Canmore, Alberta","Cardston, Alberta","Carstairs, Alberta","Castor, Alberta","Claresholm, Alberta","Coaldale, Alberta","Coalhurst, Alberta","Cochrane, Alberta","Coronation, Alberta","Crossfield, Alberta","Daysland, Alberta","Devon, Alberta","Diamond Valley, Alberta","Didsbury, Alberta","Drayton Valley, Alberta","Drumheller, Alberta","Eckville, Alberta","Edson, Alberta","Elk Point, Alberta","Fairview, Alberta","Falher, Alberta","Fort Macleod, Alberta","Fox Creek, Alberta","Gibbons, Alberta","Grimshaw, Alberta","Hanna, Alberta","Hardisty, Alberta","High Level, Alberta","High Prairie, Alberta","High River, Alberta","Hinton, Alberta","Innisfail, Alberta","Irricana, Alberta","Killam, Alberta","Lamont, Alberta","Legal, Alberta","Magrath, Alberta","Manning, Alberta","Mayerthorpe, Alberta","McLennan, Alberta","Milk River, Alberta","Millet, Alberta","Morinville, Alberta","Mundare, Alberta","Nanton, Alberta","Nobleford, Alberta","Okotoks, Alberta","Olds, Alberta","Onoway, Alberta","Oyen, Alberta","Peace River, Alberta","Penhold, Alberta","Picture Butte, Alberta","Pincher Creek, Alberta","Ponoka, Alberta","Provost, Alberta","Rainbow Lake, Alberta","Raymond, Alberta","Redcliff, Alberta","Redwater, Alberta","Rimbey, Alberta","Rocky Mountain House, Alberta","Sedgewick, Alberta","Sexsmith, Alberta","Slave Lake, Alberta","Smoky Lake, Alberta","Spirit River, Alberta","St. Paul, Alberta","Stavely, Alberta","Stettler, Alberta","Stony Plain, Alberta","Strathmore, Alberta","Sundre, Alberta","Swan Hills, Alberta","Sylvan Lake, Alberta","Taber, Alberta","Thorsby, Alberta","Three Hills, Alberta","Tofield, Alberta","Trochu, Alberta","Two Hills, Alberta","Valleyview, Alberta","Vauxhall, Alberta","Vegreville, Alberta","Vermilion, Alberta","Viking, Alberta","Vulcan, Alberta","Wainwright, Alberta","Wembley, Alberta","Westlock, Alberta","Whitecourt, Alberta","Airdrie, Alberta","Beaumont, Alberta","Brooks, Alberta","Calgary, Alberta","Camrose, Alberta","Chestermere, Alberta","Cold Lake, Alberta","Edmonton, Alberta","Fort Saskatchewan, Alberta","Grande Prairie, Alberta","Lacombe, Alberta","Leduc, Alberta","Lethbridge, Alberta","Lloydminster , Alberta","Medicine Hat, Alberta","Red Deer, Alberta","Spruce Grove, Alberta","St. Albert, Alberta","Wetaskiwin, Alberta","Comox, British Columbia","Creston, British Columbia","Gibsons, British Columbia","Golden, British Columbia","Ladysmith, British Columbia","Lake Cowichan, British Columbia","Oliver, British Columbia","Osoyoos, British Columbia","Port McNeill, British Columbia","Princeton, British Columbia","Qualicum Beach, British Columbia","Sidney, British Columbia","Smithers, British Columbia","View Royal, British Columbia","Abbotsford, British Columbia","Armstrong, British Columbia","Burnaby, British Columbia","Campbell River, British Columbia","Castlegar, British Columbia","Chilliwack, British Columbia","Colwood, British Columbia","Coquitlam, British Columbia","Courtenay, British Columbia","Cranbrook, British Columbia","Dawson Creek, British Columbia","Delta, British Columbia","Duncan, British Columbia","Enderby, British Columbia","Fernie, British Columbia","Fort St. John, British Columbia","Grand Forks, British Columbia","Greenwood, British Columbia","Kamloops, British Columbia","Kelowna, British Columbia","Kimberley, British Columbia","Langford, British Columbia","Langley, British Columbia","Maple Ridge, British Columbia","Merritt, British Columbia","Mission, British Columbia","Nanaimo, British Columbia","Nelson, British Columbia","New Westminster, British Columbia","North Vancouver, British Columbia","Parksville, British Columbia","Penticton, British Columbia","Pitt Meadows, British Columbia","Port Alberni, British Columbia","Port Coquitlam, British Columbia","Port Moody, British Columbia","Powell River, British Columbia","Prince George, British Columbia","Prince Rupert, British Columbia","Quesnel, British Columbia","Revelstoke, British Columbia","Richmond, British Columbia","Rossland, British Columbia","Salmon Arm, British Columbia","Surrey, British Columbia","Terrace, British Columbia","Trail, British Columbia","Vancouver, British Columbia","Vernon, British Columbia","Victoria, British Columbia","West Kelowna, British Columbia","White Rock, British Columbia","Williams Lake, British Columbia","Altona, Manitoba","Arborg, Manitoba","Beausejour, Manitoba","Carberry, Manitoba","Carman, Manitoba","Churchill, Manitoba","Gillam, Manitoba","Grand Rapids, Manitoba","Lac du Bonnet, Manitoba","Leaf Rapids, Manitoba","Lynn Lake, Manitoba","Melita, Manitoba","Minnedosa, Manitoba","Morris, Manitoba","Neepawa, Manitoba","Niverville, Manitoba","The Pas, Manitoba","Powerview-Pine Falls, Manitoba","Snow Lake, Manitoba","Ste. Anne, Manitoba","Stonewall, Manitoba","Swan River, Manitoba","Teulon, Manitoba","Virden, Manitoba","Winnipeg Beach, Manitoba","Brandon, Manitoba","Dauphin, Manitoba","Flin Flon , Manitoba","Morden, Manitoba","Portage la Prairie, Manitoba","Selkirk, Manitoba","Steinbach, Manitoba","Thompson, Manitoba","Winkler, Manitoba","Winnipeg, Manitoba","Bathurst, New Brunswick","Campbellton, New Brunswick","Dieppe, New Brunswick","Edmundston, New Brunswick","Fredericton, New Brunswick","Miramichi, New Brunswick","Moncton, New Brunswick","Saint John, New Brunswick","Tracadie, New Brunswick","Beaubassin East, New Brunswick","Campobello Island, New Brunswick","Cocagne, New Brunswick","Hanwell, New Brunswick","Haut-Madawaska, New Brunswick","Kedgwick, New Brunswick","Saint-André, New Brunswick","Upper Miramichi, New Brunswick","Beresford, New Brunswick","Bouctouche, New Brunswick","Caraquet, New Brunswick","Dalhousie, New Brunswick","Florenceville-Bristol, New Brunswick","Grand Bay-Westfield, New Brunswick","Grand Falls, New Brunswick","Hampton, New Brunswick","Hartland, New Brunswick","Lamèque, New Brunswick","Nackawic, New Brunswick","Oromocto, New Brunswick","Quispamsis, New Brunswick","Richibucto, New Brunswick","Riverview, New Brunswick","Rothesay, New Brunswick","Sackville, New Brunswick","Saint Andrews, New Brunswick","Saint-Léonard, New Brunswick","Saint-Quentin, New Brunswick","Shediac, New Brunswick","Shippagan, New Brunswick","St. George, New Brunswick","St. Stephen, New Brunswick","Sussex, New Brunswick","Woodstock, New Brunswick","Alma, New Brunswick","Aroostook, New Brunswick","Atholville, New Brunswick","Balmoral, New Brunswick","Bas-Caraquet, New Brunswick","Bath, New Brunswick","Belledune, New Brunswick","Bertrand, New Brunswick","Blacks Harbour, New Brunswick","Blackville, New Brunswick","Cambridge-Narrows, New Brunswick","Canterbury, New Brunswick","Cap-Pelé, New Brunswick","Centreville, New Brunswick","Charlo, New Brunswick","Chipman, New Brunswick","Doaktown, New Brunswick","Dorchester, New Brunswick","Drummond, New Brunswick","Eel River Crossing, New Brunswick","Fredericton Junction, New Brunswick","Gagetown, New Brunswick","Grand Manan, New Brunswick","Grande-Anse, New Brunswick","Harvey, New Brunswick","Hillsborough, New Brunswick","Lac Baker, New Brunswick","Le Goulet, New Brunswick","Maisonnette, New Brunswick","McAdam, New Brunswick","Meductic, New Brunswick","Memramcook, New Brunswick","Millville, New Brunswick","Minto, New Brunswick","Neguac, New Brunswick","New Maryland, New Brunswick","Nigadoo, New Brunswick","Norton, New Brunswick","Paquetville, New Brunswick","Perth-Andover, New Brunswick","Petitcodiac, New Brunswick","Petit-Rocher, New Brunswick","Plaster Rock, New Brunswick","Pointe-Verte, New Brunswick","Port Elgin, New Brunswick","Rexton, New Brunswick","Riverside-Albert, New Brunswick","Rivière-Verte, New Brunswick","Rogersville, New Brunswick","Saint-Antoine, New Brunswick","Sainte-Anne-de-Madawaska, New Brunswick","Sainte-Marie-Saint-Raphaël, New Brunswick","Saint-Isidore, New Brunswick","Saint-Léolin, New Brunswick","Saint-Louis de Kent, New Brunswick","Salisbury, New Brunswick","St. Martins, New Brunswick","Stanley, New Brunswick","Sussex Corner, New Brunswick","Tide Head, New Brunswick","Tracy, New Brunswick","Bathurst, New Brunswick","Campbellton, New Brunswick","Dieppe, New Brunswick","Edmundston, New Brunswick","Fredericton, New Brunswick","Miramichi, New Brunswick","Moncton, New Brunswick","Saint John, New Brunswick","Corner Brook, Newfoundland and Labrador ","Mount Pearl, Newfoundland and Labrador ","St. John's, Newfoundland and Labrador ","Admirals Beach, Newfoundland and Labrador ","Anchor Point, Newfoundland and Labrador ","Appleton, Newfoundland and Labrador ","Aquaforte, Newfoundland and Labrador ","Arnold's Cove, Newfoundland and Labrador ","Avondale, Newfoundland and Labrador ","Badger, Newfoundland and Labrador ","Baie Verte, Newfoundland and Labrador ","Baine Harbour, Newfoundland and Labrador ","Bauline, Newfoundland and Labrador ","Bay Bulls, Newfoundland and Labrador ","Bay de Verde, Newfoundland and Labrador ","Bay L'Argent, Newfoundland and Labrador ","Bay Roberts, Newfoundland and Labrador ","Baytona, Newfoundland and Labrador ","Beachside, Newfoundland and Labrador ","Bellburns, Newfoundland and Labrador ","Belleoram, Newfoundland and Labrador ","Birchy Bay, Newfoundland and Labrador ","Bird Cove, Newfoundland and Labrador ","Bishop's Cove, Newfoundland and Labrador ","Bishop's Falls, Newfoundland and Labrador ","Bonavista, Newfoundland and Labrador ","Botwood, Newfoundland and Labrador ","Branch, Newfoundland and Labrador ","Brent's Cove, Newfoundland and Labrador ","Brighton, Newfoundland and Labrador ","Brigus, Newfoundland and Labrador ","Bryant's Cove, Newfoundland and Labrador ","Buchans, Newfoundland and Labrador ","Burgeo, Newfoundland and Labrador ","Burin, Newfoundland and Labrador ","Burlington, Newfoundland and Labrador ","Burnt Islands, Newfoundland and Labrador ","Campbellton, Newfoundland and Labrador ","Cape Broyle, Newfoundland and Labrador ","Cape St. George, Newfoundland and Labrador ","Carbonear, Newfoundland and Labrador ","Carmanville, Newfoundland and Labrador ","Cartwright, Labrador, Newfoundland and Labrador ","Centreville-Wareham-Trinity, Newfoundland and Labrador ","Chance Cove, Newfoundland and Labrador ","Change Islands, Newfoundland and Labrador ","Channel-Port aux Basques, Newfoundland and Labrador ","Chapel Arm, Newfoundland and Labrador ","Charlottetown, Newfoundland and Labrador ","Clarenville, Newfoundland and Labrador ","Clarke's Beach, Newfoundland and Labrador ","Coachman's Cove, Newfoundland and Labrador ","Colinet, Newfoundland and Labrador ","Colliers, Newfoundland and Labrador ","Come By Chance, Newfoundland and Labrador ","Comfort Cove-Newstead, Newfoundland and Labrador ","Conception Bay South, Newfoundland and Labrador ","Conception Harbour, Newfoundland and Labrador ","Conche, Newfoundland and Labrador ","Cook's Harbour, Newfoundland and Labrador ","Cormack, Newfoundland and Labrador ","Cottlesville, Newfoundland and Labrador ","Cow Head, Newfoundland and Labrador ","Cox's Cove, Newfoundland and Labrador ","Crow Head, Newfoundland and Labrador ","Cupids, Newfoundland and Labrador ","Daniel's Harbour, Newfoundland and Labrador ","Deer Lake, Newfoundland and Labrador ","Dover, Newfoundland and Labrador ","Duntara, Newfoundland and Labrador ","Eastport, Newfoundland and Labrador ","Elliston, Newfoundland and Labrador ","Embree, Newfoundland and Labrador ","Englee, Newfoundland and Labrador ","English Harbour East, Newfoundland and Labrador ","Fermeuse, Newfoundland and Labrador ","Ferryland, Newfoundland and Labrador ","Flatrock, Newfoundland and Labrador ","Fleur de Lys, Newfoundland and Labrador ","Flower's Cove, Newfoundland and Labrador ","Fogo Island, Newfoundland and Labrador ","Forteau, Newfoundland and Labrador ","Fortune, Newfoundland and Labrador ","Fox Cove-Mortier, Newfoundland and Labrador ","Fox Harbour, Newfoundland and Labrador ","Frenchman's Cove, Newfoundland and Labrador ","Gallants, Newfoundland and Labrador ","Gambo, Newfoundland and Labrador ","Gander, Newfoundland and Labrador ","Garnish, Newfoundland and Labrador ","Gaskiers-Point La Haye, Newfoundland and Labrador ","Gaultois, Newfoundland and Labrador ","Gillams, Newfoundland and Labrador ","Glenburnie-Birchy Head-Shoal Brook, Newfoundland and Labrador ","Glenwood, Newfoundland and Labrador ","Glovertown, Newfoundland and Labrador ","Goose Cove East, Newfoundland and Labrador ","Grand Bank, Newfoundland and Labrador ","Grand Falls-Windsor, Newfoundland and Labrador ","Grand le Pierre, Newfoundland and Labrador ","Greenspond, Newfoundland and Labrador ","Hampden, Newfoundland and Labrador ","Hant's Harbour, Newfoundland and Labrador ","Happy Adventure, Newfoundland and Labrador ","Happy Valley-Goose Bay, Newfoundland and Labrador ","Harbour Breton, Newfoundland and Labrador ","Harbour Grace, Newfoundland and Labrador ","Harbour Main-Chapel's Cove-Lakeview, Newfoundland and Labrador ","Hare Bay, Newfoundland and Labrador ","Hawke's Bay, Newfoundland and Labrador ","Heart's Content, Newfoundland and Labrador ","Heart's Delight-Islington, Newfoundland and Labrador ","Heart's Desire, Newfoundland and Labrador ","Hermitage-Sandyville, Newfoundland and Labrador ","Holyrood, Newfoundland and Labrador ","Howley, Newfoundland and Labrador ","Hughes Brook, Newfoundland and Labrador ","Humber Arm South, Newfoundland and Labrador ","Indian Bay, Newfoundland and Labrador ","Irishtown-Summerside, Newfoundland and Labrador ","Isle aux Morts, Newfoundland and Labrador ","Jackson's Arm, Newfoundland and Labrador ","Keels, Newfoundland and Labrador ","King's Cove, Newfoundland and Labrador ","King's Point, Newfoundland and Labrador ","Kippens, Newfoundland and Labrador ","Labrador City, Newfoundland and Labrador ","Lamaline, Newfoundland and Labrador ","L'Anse-au-Clair, Newfoundland and Labrador ","L'Anse-au-Loup, Newfoundland and Labrador ","Lark Harbour, Newfoundland and Labrador ","LaScie, Newfoundland and Labrador ","Lawn, Newfoundland and Labrador ","Leading Tickles, Newfoundland and Labrador ","Lewin's Cove, Newfoundland and Labrador ","Lewisporte, Newfoundland and Labrador ","Little Bay, Newfoundland and Labrador ","Little Bay East, Newfoundland and Labrador ","Little Bay Islands, Newfoundland and Labrador ","Little Burnt Bay, Newfoundland and Labrador ","Logy Bay-Middle Cove-Outer Cove, Newfoundland and Labrador ","Long Harbour-Mount Arlington Heights, Newfoundland and Labrador ","Lord's Cove, Newfoundland and Labrador ","Lourdes, Newfoundland and Labrador ","Lumsden, Newfoundland and Labrador ","Lushes Bight-Beaumont-Beaumont North, Newfoundland and Labrador ","Main Brook, Newfoundland and Labrador ","Mary's Harbour, Newfoundland and Labrador ","Marystown, Newfoundland and Labrador ","Massey Drive, Newfoundland and Labrador ","McIvers, Newfoundland and Labrador ","Meadows, Newfoundland and Labrador ","Middle Arm, Newfoundland and Labrador ","Miles Cove, Newfoundland and Labrador ","Millertown, Newfoundland and Labrador ","Milltown-Head of Bay d'Espoir, Newfoundland and Labrador ","Ming's Bight, Newfoundland and Labrador ","Morrisville, Newfoundland and Labrador ","Mount Carmel-Mitchells Brook-St. Catherines, Newfoundland and Labrador ","Mount Moriah, Newfoundland and Labrador ","Musgrave Harbour, Newfoundland and Labrador ","Musgravetown, Newfoundland and Labrador ","New Perlican, Newfoundland and Labrador ","New-Wes-Valley, Newfoundland and Labrador ","Nipper's Harbour, Newfoundland and Labrador ","Norman's Cove-Long Cove, Newfoundland and Labrador ","Norris Arm, Newfoundland and Labrador ","Norris Point, Newfoundland and Labrador ","North River, Newfoundland and Labrador ","North West River, Newfoundland and Labrador ","Northern Arm, Newfoundland and Labrador ","Old Perlican, Newfoundland and Labrador ","Pacquet, Newfoundland and Labrador ","Paradise, Newfoundland and Labrador ","Parkers Cove, Newfoundland and Labrador ","Parson's Pond, Newfoundland and Labrador ","Pasadena, Newfoundland and Labrador ","Peterview, Newfoundland and Labrador ","Petty Harbour-Maddox Cove, Newfoundland and Labrador ","Pilley's Island, Newfoundland and Labrador ","Pinware, Newfoundland and Labrador ","Placentia, Newfoundland and Labrador ","Point au Gaul, Newfoundland and Labrador ","Point Lance, Newfoundland and Labrador ","Point Leamington, Newfoundland and Labrador ","Point May, Newfoundland and Labrador ","Point of Bay, Newfoundland and Labrador ","Pool's Cove, Newfoundland and Labrador ","Port Anson, Newfoundland and Labrador ","Port au Choix, Newfoundland and Labrador ","Port au Port East, Newfoundland and Labrador ","Port au Port West-Aguathuna-Felix Cove, Newfoundland and Labrador ","Port Blandford, Newfoundland and Labrador ","Port Hope Simpson, Newfoundland and Labrador ","Port Kirwan, Newfoundland and Labrador ","Port Rexton, Newfoundland and Labrador ","Port Saunders, Newfoundland and Labrador ","Portugal Cove South, Newfoundland and Labrador ","Portugal Cove–St. Philip's, Newfoundland and Labrador ","Pouch Cove, Newfoundland and Labrador ","Raleigh, Newfoundland and Labrador ","Ramea, Newfoundland and Labrador ","Red Bay, Newfoundland and Labrador ","Red Harbour, Newfoundland and Labrador ","Reidville, Newfoundland and Labrador ","Rencontre East, Newfoundland and Labrador ","Renews-Cappahayden, Newfoundland and Labrador ","River of Ponds, Newfoundland and Labrador ","Riverhead, Newfoundland and Labrador ","Robert's Arm, Newfoundland and Labrador ","Rocky Harbour, Newfoundland and Labrador ","Roddickton-Bide Arm, Newfoundland and Labrador ","Rose Blanche-Harbour le Cou, Newfoundland and Labrador ","Rushoon, Newfoundland and Labrador ","Sally's Cove, Newfoundland and Labrador ","Salmon Cove, Newfoundland and Labrador ","Salvage, Newfoundland and Labrador ","Sandringham, Newfoundland and Labrador ","Sandy Cove, Newfoundland and Labrador ","Seal Cove (Fortune Bay), Newfoundland and Labrador ","Seal Cove (White Bay), Newfoundland and Labrador ","Small Point-Adam's Cove-Blackhead-Broad Cove, Newfoundland and Labrador ","South Brook, Newfoundland and Labrador ","South River, Newfoundland and Labrador ","Southern Harbour, Newfoundland and Labrador ","Spaniard's Bay, Newfoundland and Labrador ","Springdale, Newfoundland and Labrador ","St. Alban's, Newfoundland and Labrador ","St. Anthony, Newfoundland and Labrador ","St. Bernard's-Jacques Fontaine, Newfoundland and Labrador ","St. Brendan's, Newfoundland and Labrador ","St. Bride's, Newfoundland and Labrador ","St. George's, Newfoundland and Labrador ","St. Jacques-Coomb's Cove, Newfoundland and Labrador ","St. Joseph's, Newfoundland and Labrador ","St. Lawrence, Newfoundland and Labrador ","St. Lewis, Newfoundland and Labrador ","St. Lunaire-Griquet, Newfoundland and Labrador ","St. Mary's, Newfoundland and Labrador ","St. Pauls, Newfoundland and Labrador ","St. Shott's, Newfoundland and Labrador ","St. Vincent's-St. Stephen's-Peter's River, Newfoundland and Labrador ","Steady Brook, Newfoundland and Labrador ","Stephenville, Newfoundland and Labrador ","Stephenville Crossing, Newfoundland and Labrador ","Summerford, Newfoundland and Labrador ","Sunnyside, Newfoundland and Labrador ","Terra Nova, Newfoundland and Labrador ","Terrenceville, Newfoundland and Labrador ","Tilt Cove, Newfoundland and Labrador ","Torbay, Newfoundland and Labrador ","Traytown, Newfoundland and Labrador ","Trepassey, Newfoundland and Labrador ","Trinity, Newfoundland and Labrador ","Trinity Bay North, Newfoundland and Labrador ","Triton, Newfoundland and Labrador ","Trout River, Newfoundland and Labrador ","Twillingate, Newfoundland and Labrador ","Upper Island Cove, Newfoundland and Labrador ","Victoria, Newfoundland and Labrador ","Wabana, Newfoundland and Labrador ","Wabush, Newfoundland and Labrador ","West St. Modeste, Newfoundland and Labrador ","Westport, Newfoundland and Labrador ","Whitbourne, Newfoundland and Labrador ","Whiteway, Newfoundland and Labrador ","Winterland, Newfoundland and Labrador ","Winterton, Newfoundland and Labrador ","Witless Bay, Newfoundland and Labrador ","Woodstock, Newfoundland and Labrador ","Woody Point, Bonne Bay, Newfoundland and Labrador ","York Harbour, Newfoundland and Labrador ","Hopedale, Newfoundland and Labrador ","Makkovik, Newfoundland and Labrador ","Nain, Newfoundland and Labrador ","Postville, Newfoundland and Labrador ","Rigolet, Newfoundland and Labrador ","Corner Brook, Newfoundland and Labrador ","Mount Pearl, Newfoundland and Labrador ","St. John's, Newfoundland and Labrador ","Fort Smith, Northwest Territories","Hay River, Northwest Territories","Inuvik, Northwest Territories","Norman Wells, Northwest Territories","Amherst, Nova Scotia","Annapolis Royal, Nova Scotia","Antigonish, Nova Scotia","Berwick, Nova Scotia","Bridgewater, Nova Scotia","Clark's Harbour, Nova Scotia","Digby, Nova Scotia","Kentville, Nova Scotia","Lockeport, Nova Scotia","Lunenburg, Nova Scotia","Mahone Bay, Nova Scotia","Middleton, Nova Scotia","Mulgrave, Nova Scotia","New Glasgow, Nova Scotia","Oxford, Nova Scotia","Pictou, Nova Scotia","Port Hawkesbury, Nova Scotia","Shelburne, Nova Scotia","Stellarton, Nova Scotia","Stewiacke, Nova Scotia","Trenton, Nova Scotia","Truro, Nova Scotia","Westville, Nova Scotia","Wolfville, Nova Scotia","Yarmouth, Nova Scotia","Annapolis, Nova Scotia","Antigonish, Nova Scotia","Cape Bretona, Nova Scotia","Colchester, Nova Scotia","Cumberland, Nova Scotia","Digby, Nova Scotia","Guysborough, Nova Scotia","Halifaxb, Nova Scotia","Hants, Nova Scotia","Inverness, Nova Scotia","Kings, Nova Scotia","Lunenburg, Nova Scotia","Pictou, Nova Scotia","Queensc, Nova Scotia","Richmond, Nova Scotia","Shelburne, Nova Scotia","Victoria, Nova Scotia","Yarmouth, Nova Scotia","Ajax, Ontario","Amherstburg, Ontario","Arnprior, Ontario","Atikokan, Ontario","Aurora, Ontario","Aylmer, Ontario","Bancroft, Ontario","Blind River, Ontario","Bracebridge, Ontario","Bradford West Gwillimbury, Ontario","Bruce Mines, Ontario","Caledon, Ontario","Carleton Place, Ontario","Cobalt, Ontario","Cobourg, Ontario","Cochrane, Ontario","Collingwood, Ontario","Deep River, Ontario","Deseronto, Ontario","East Gwillimbury, Ontario","Englehart, Ontario","Erin, Ontario","Espanola, Ontario","Essex, Ontario","Fort Erie, Ontario","Fort Frances, Ontario","Gananoque, Ontario","Georgina, Ontario","Goderich, Ontario","Gore Bay, Ontario","Grand Valley, Ontario","Gravenhurst, Ontario","Greater Napanee, Ontario","Grimsby, Ontario","Halton Hills, Ontario","Hanover, Ontario","Hawkesbury, Ontario","Hearst, Ontario","Huntsville, Ontario","Ingersoll, Ontario","Innisfil, Ontario","Iroquois Falls, Ontario","Kapuskasing, Ontario","Kearney, Ontario","Kingsville, Ontario","Kirkland Lake, Ontario","Lakeshore, Ontario","LaSalle, Ontario","Latchford, Ontario","Laurentian Hills, Ontario","Lincoln, Ontario","Marathon, Ontario","Mattawa, Ontario","Midland, Ontario","Milton, Ontario","Minto, Ontario","Mississippi Mills, Ontario","Mono, Ontario","Moosonee, Ontario","New Tecumseth, Ontario","Newmarket, Ontario","Niagara-on-the-Lake, Ontario","Northeastern Manitoulin and the Islands, Ontario","Oakville, Ontario","Orangeville, Ontario","Parry Sound, Ontario","Pelham, Ontario","Penetanguishene, Ontario","Perth, Ontario","Petawawa, Ontario","Petrolia, Ontario","Plympton-Wyoming, Ontario","Prescott, Ontario","Rainy River, Ontario","Renfrew, Ontario","Saugeen Shores, Ontario","Shelburne, Ontario","Smiths Falls, Ontario","Smooth Rock Falls, Ontario","South Bruce Peninsula, Ontario","Spanish, Ontario","St. Marys, Ontario","Tecumseh, Ontario","The Blue Mountains, Ontario","Thessalon, Ontario","Tillsonburg, Ontario","Wasaga Beach, Ontario","Whitby, Ontario","Whitchurch-Stouffville, Ontario","Barrie, Ontario","Belleville, Ontario","Brampton, Ontario","Brant, Ontario","Brantford, Ontario","Brockville, Ontario","Burlington, Ontario","Cambridge, Ontario","Clarence-Rockland, Ontario","Cornwall, Ontario","Dryden, Ontario","Elliot Lake, Ontario","Greater Sudbury, Ontario","Guelph, Ontario","Haldimand County, Ontario","Hamilton, Ontario","Kawartha Lakes, Ontario","Kenora, Ontario","Kingston, Ontario","Kitchener, Ontario","London, Ontario","Markham, Ontario","Mississauga, Ontario","Niagara Falls, Ontario","Norfolk County, Ontario","North Bay, Ontario","Orillia, Ontario","Oshawa, Ontario","Ottawa, Ontario","Owen Sound, Ontario","Pembroke, Ontario","Peterborough, Ontario","Pickering, Ontario","Port Colborne, Ontario","Prince Edward County, Ontario","Quinte West, Ontario","Richmond Hill, Ontario","Sarnia, Ontario","Sault Ste. Marie, Ontario","St. Catharines, Ontario","St. Thomas, Ontario","Stratford, Ontario","Temiskaming Shores, Ontario","Thorold, Ontario","Thunder Bay, Ontario","Timmins, Ontario","Toronto, Ontario","Vaughan, Ontario","Waterloo, Ontario","Welland, Ontario","Windsor, Ontario","Woodstock, Ontario","Alberton, Prince Edward Island","Borden-Carleton, Prince Edward Island","Cornwall, Prince Edward Island","Kensington, Prince Edward Island","North Rustico, Prince Edward Island","O'Leary, Prince Edward Island","Souris, Prince Edward Island","Stratford, Prince Edward Island","Three Rivers, Prince Edward Island","Tignish, Prince Edward Island","Charlottetown, Prince Edward Island","Summerside, Prince Edward Island","Acton Vale, Quebec","Alma, Quebec","Amos, Quebec","Amqui, Quebec","Baie-Comeau, Quebec","Baie-D'Urfé, Quebec","Baie-Saint-Paul, Quebec","Barkmere, Quebec","Beaconsfield, Quebec","Beauceville, Quebec","Beauharnois, Quebec","Beaupré, Quebec","Bécancour, Quebec","Bedford, Quebec","Belleterre, Quebec","Beloeil, Quebec","Berthierville, Quebec","Blainville, Quebec","Boisbriand, Quebec","Bois-des-Filion, Quebec","Bonaventure, Quebec","Boucherville, Quebec","Lac-Brome, Quebec","Bromont, Quebec","Brossard, Quebec","Brownsburg-Chatham, Quebec","Candiac, Quebec","Cap-Chat, Quebec","Cap-Santé, Quebec","Carignan, Quebec","Carleton-sur-Mer, Quebec","Causapscal, Quebec","Chambly, Quebec","Chandler, Quebec","Chapais, Quebec","Charlemagne, Quebec","Châteauguay, Quebec","Château-Richer, Quebec","Chibougamau, Quebec","Clermont, Quebec","Coaticook, Quebec","Contrecoeur, Quebec","Cookshire-Eaton, Quebec","Côte Saint-Luc, Quebec","Coteau-du-Lac, Quebec","Cowansville, Quebec","Danville, Quebec","Daveluyville, Quebec","Dégelis, Quebec","Delson, Quebec","Desbiens, Quebec","Deux-Montagnes, Quebec","Disraeli, Quebec","Dolbeau-Mistassini, Quebec","Dollard-des-Ormeaux, Quebec","Donnacona, Quebec","Dorval, Quebec","Drummondville, Quebec","Dunham, Quebec","Duparquet, Quebec","East Angus, Quebec","Estérel, Quebec","Farnham, Quebec","Fermont, Quebec","Forestville, Quebec","Fossambault-sur-le-Lac, Quebec","Gaspé, Quebec","Gatineau, Quebec","Gracefield, Quebec","Granby, Quebec","Grande-Rivière, Quebec","Hampstead, Quebec","Hudson, Quebec","Huntingdon, Quebec","Joliette, Quebec","Kingsey Falls, Quebec","Kirkland, Quebec","La Malbaie, Quebec","La Pocatière, Quebec","La Prairie, Quebec","La Sarre, Quebec","La Tuque[QC 1], Quebec","Lac-Delage, Quebec","Lachute, Quebec","Lac-Mégantic, Quebec","Lac-Saint-Joseph, Quebec","Lac-Sergent, Quebec","L'Ancienne-Lorette, Quebec","L'Assomption, Quebec","Laval, Quebec","Lavaltrie, Quebec","Lebel-sur-Quévillon, Quebec","L'Épiphanie, Quebec","Léry, Quebec","Lévis, Quebec","L'Île-Cadieux, Quebec","L'Île-Dorval, Quebec","L'Île-Perrot, Quebec","Longueuil, Quebec","Lorraine, Quebec","Louiseville, Quebec","Macamic, Quebec","Magog, Quebec","Malartic, Quebec","Maniwaki, Quebec","Marieville, Quebec","Mascouche, Quebec","Matagami, Quebec","Matane, Quebec","Mercier, Quebec","Métabetchouan–Lac-à-la-Croix, Quebec","Métis-sur-Mer, Quebec","Mirabel, Quebec","Mont-Joli, Quebec","Mont-Laurier, Quebec","Montmagny, Quebec","Montreal[QC 3], Quebec","Montreal West, Quebec","Montréal-Est, Quebec","Mont-Saint-Hilaire, Quebec","Mont-Tremblant, Quebec","Mount Royal, Quebec","Murdochville, Quebec","Neuville, Quebec","New Richmond, Quebec","Nicolet, Quebec","Normandin, Quebec","Notre-Dame-de-l'Île-Perrot, Quebec","Notre-Dame-des-Prairies, Quebec","Otterburn Park, Quebec","Paspébiac, Quebec","Percé, Quebec","Pincourt, Quebec","Plessisville, Quebec","Pohénégamook, Quebec","Pointe-Claire, Quebec","Pont-Rouge, Quebec","Port-Cartier, Quebec","Portneuf, Quebec","Prévost, Quebec","Princeville, Quebec","Québec[QC 4], Quebec","Repentigny, Quebec","Richelieu, Quebec","Richmond, Quebec","Rigaud, Quebec","Rimouski, Quebec","Rivière-du-Loup, Quebec","Rivière-Rouge, Quebec","Roberval, Quebec","Rosemère, Quebec","Rouyn-Noranda, Quebec","Saguenay, Quebec","Saint-Amable, Quebec","Saint-Augustin-de-Desmaures, Quebec","Saint-Basile, Quebec","Saint-Basile-le-Grand, Quebec","Saint-Bruno-de-Montarville, Quebec","Saint-Césaire, Quebec","Saint-Charles-Borromée, Quebec","Saint-Colomban, Quebec","Saint-Constant, Quebec","Sainte-Adèle, Quebec","Sainte-Agathe-des-Monts, Quebec","Sainte-Anne-de-Beaupré, Quebec","Sainte-Anne-de-Bellevue, Quebec","Sainte-Anne-des-Monts, Quebec","Sainte-Anne-des-Plaines, Quebec","Sainte-Catherine, Quebec","Sainte-Catherine-de-la-Jacques-Cartier, Quebec","Sainte-Julie, Quebec","Sainte-Marguerite-du-Lac-Masson, Quebec","Sainte-Marie, Quebec","Sainte-Marthe-sur-le-Lac, Quebec","Sainte-Thérèse, Quebec","Saint-Eustache, Quebec","Saint-Félicien, Quebec","Saint-Gabriel, Quebec","Saint-Georges, Quebec","Saint-Hyacinthe, Quebec","Saint-Jean-sur-Richelieu, Quebec","Saint-Jérôme, Quebec","Saint-Joseph-de-Beauce, Quebec","Saint-Joseph-de-Sorel, Quebec","Saint-Lambert, Quebec","Saint-Lazare, Quebec","Saint-Lin–Laurentides, Quebec","Saint-Marc-des-Carrières, Quebec","Saint-Ours, Quebec","Saint-Pamphile, Quebec","Saint-Pascal, Quebec","Saint-Philippe, Quebec","Saint-Pie, Quebec","Saint-Raymond, Quebec","Saint-Rémi, Quebec","Saint-Sauveur, Quebec","Saint-Tite, Quebec","Salaberry-de-Valleyfield, Quebec","Schefferville, Quebec","Scotstown, Quebec","Senneterre, Quebec","Sept-Îles, Quebec","Shannon, Quebec","Shawinigan, Quebec","Sherbrooke, Quebec","Sorel-Tracy, Quebec","Stanstead, Quebec","Sutton, Quebec","Témiscaming, Quebec","Témiscouata-sur-le-Lac, Quebec","Terrebonne, Quebec","Thetford Mines, Quebec","Thurso, Quebec","Trois-Pistoles, Quebec","Trois-Rivières, Quebec","Valcourt, Quebec","Val-d'Or, Quebec","Val-des-Sources, Quebec","Varennes, Quebec","Vaudreuil-Dorion, Quebec","Victoriaville, Quebec","Ville-Marie, Quebec","Warwick, Quebec","Waterloo, Quebec","Waterville, Quebec","Westmount, Quebec","Windsor, Quebec","Aberdeen, Saskatchewan","Alameda, Saskatchewan","Allan, Saskatchewan","Arborfield, Saskatchewan","Arcola, Saskatchewan","Asquith, Saskatchewan","Assiniboia, Saskatchewan","Balcarres, Saskatchewan","Balgonie, Saskatchewan","Battleford, Saskatchewan","Bengough, Saskatchewan","Bienfait, Saskatchewan","Big River, Saskatchewan","Biggar, Saskatchewan","Birch Hills, Saskatchewan","Blaine Lake, Saskatchewan","Bredenbury, Saskatchewan","Broadview, Saskatchewan","Bruno, Saskatchewan","Burstall, Saskatchewan","Cabri, Saskatchewan","Canora, Saskatchewan","Carlyle, Saskatchewan","Carnduff, Saskatchewan","Carrot River, Saskatchewan","Central Butte, Saskatchewan","Choiceland, Saskatchewan","Churchbridge, Saskatchewan","Colonsay, Saskatchewan","Coronach, Saskatchewan","Craik, Saskatchewan","Cudworth, Saskatchewan","Cupar, Saskatchewan","Cut Knife, Saskatchewan","Dalmeny, Saskatchewan","Davidson, Saskatchewan","Delisle, Saskatchewan","Duck Lake, Saskatchewan","Dundurn, Saskatchewan","Eastend, Saskatchewan","Eatonia, Saskatchewan","Elrose, Saskatchewan","Esterhazy, Saskatchewan","Eston, Saskatchewan","Fleming, Saskatchewan","Foam Lake, Saskatchewan","Fort Qu'Appelle, Saskatchewan","Francis, Saskatchewan","Govan, Saskatchewan","Grand Coulee, Saskatchewan","Gravelbourg, Saskatchewan","Grenfell, Saskatchewan","Gull Lake, Saskatchewan","Hafford, Saskatchewan","Hague, Saskatchewan","Hanley, Saskatchewan","Hepburn, Saskatchewan","Herbert, Saskatchewan","Hudson Bay, Saskatchewan","Imperial, Saskatchewan","Indian Head, Saskatchewan","Ituna, Saskatchewan","Kamsack, Saskatchewan","Kelvington, Saskatchewan","Kerrobert, Saskatchewan","Kindersley, Saskatchewan","Kinistino, Saskatchewan","Kipling, Saskatchewan","Kyle, Saskatchewan","Lafleche, Saskatchewan","Lampman, Saskatchewan","Langenburg, Saskatchewan","Langham, Saskatchewan","Lanigan, Saskatchewan","Lashburn, Saskatchewan","Leader, Saskatchewan","Lemberg, Saskatchewan","Leroy, Saskatchewan","Lumsden, Saskatchewan","Luseland, Saskatchewan","Macklin, Saskatchewan","Maidstone, Saskatchewan","Maple Creek, Saskatchewan","Marshall, Saskatchewan","Midale, Saskatchewan","Milestone, Saskatchewan","Moosomin, Saskatchewan","Morse, Saskatchewan","Mossbank, Saskatchewan","Naicam, Saskatchewan","Nipawin, Saskatchewan","Nokomis, Saskatchewan","Norquay, Saskatchewan","Ogema, Saskatchewan","Osler, Saskatchewan","Outlook, Saskatchewan","Oxbow, Saskatchewan","Pense, Saskatchewan","Pilot Butte, Saskatchewan","Ponteix, Saskatchewan","Porcupine Plain, Saskatchewan","Preeceville, Saskatchewan","Qu'Appelle, Saskatchewan","Radisson, Saskatchewan","Radville, Saskatchewan","Raymore, Saskatchewan","Redvers, Saskatchewan","Regina Beach, Saskatchewan","Rocanville, Saskatchewan","Rockglen, Saskatchewan","Rose Valley, Saskatchewan","Rosetown, Saskatchewan","Rosthern, Saskatchewan","Rouleau, Saskatchewan","Saltcoats, Saskatchewan","Scott, Saskatchewan","Shaunavon, Saskatchewan","Shellbrook, Saskatchewan","Sintaluta, Saskatchewan","Southey, Saskatchewan","Spiritwood, Saskatchewan","Springside, Saskatchewan","St. Brieux, Saskatchewan","St. Walburg, Saskatchewan","Star City, Saskatchewan","Stoughton, Saskatchewan","Strasbourg, Saskatchewan","Sturgis, Saskatchewan","Tisdale, Saskatchewan","Turtleford, Saskatchewan","Unity, Saskatchewan","Vonda, Saskatchewan","Wadena, Saskatchewan","Wakaw, Saskatchewan","Waldheim, Saskatchewan","Wapella, Saskatchewan","Watrous, Saskatchewan","Watson, Saskatchewan","Wawota, Saskatchewan","White City, Saskatchewan","Whitewood, Saskatchewan","Wilkie, Saskatchewan","Willow Bunch, Saskatchewan","Wolseley, Saskatchewan","Wynyard, Saskatchewan","Yellow Grass, Saskatchewan","Zealandia, Saskatchewan","Estevan, Saskatchewan","Flin Flon , Saskatchewan","Humboldt, Saskatchewan","Lloydminster, Saskatchewan","Martensville, Saskatchewan","Meadow Lake, Saskatchewan","Melfort, Saskatchewan","Melville, Saskatchewan","Moose Jaw, Saskatchewan","North Battleford, Saskatchewan","Prince Albert, Saskatchewan","Regina, Saskatchewan","Saskatoon, Saskatchewan","Swift Current, Saskatchewan","Warman, Saskatchewan","Weyburn, Saskatchewan","Yorkton, Saskatchewan","Dawson City, Yukon","Faro, Yukon","Watson Lake, Yukon","Whitehorse, Yukon","Arctic Bay, Nunavut","Arviat, Nunavut","Baker Lake, Nunavut","Bathurst Inletc, Nunavut","Cambridge Bay, Nunavut","Chesterfield Inlet, Nunavut","Clyde River, Nunavut","Coral Harbour, Nunavut","Gjoa Haven, Nunavut","Grise Fiord, Nunavut","Igloolik, Nunavut","Kimmirut, Nunavut","Kinngait, Nunavut","Kugaaruk, Nunavut","Kugluktuk, Nunavut","Nanisivikc, Nunavut","Naujaat, Nunavut","Pangnirtung, Nunavut","Pond Inlet, Nunavut","Qikiqtarjuaq, Nunavut","Rankin Inlet, Nunavut","Resolute, Nunavut","Sanikiluaq, Nunavut","Sanirajak, Nunavut","Taloyoak, Nunavut","Umingmaktokc, Nunavut","Whale Cove, Nunavut","Iqaluit, Nunavut"

#Random choice
rand_name = random.choice(places)
    
# App menu Random Location item Child window
def my_w_child_randloc():
    my_w_child_randloc=Toplevel(root)  
    my_w_child_randloc.geometry("1000x500")  
    my_w_child_randloc.title("Random Location")
    my_w_child_randloc.configure(bg='black')  
    
    canvas= Canvas(my_w_child_randloc, width= 1920, height= 1080, bg="black")

    # text in Canvas
    canvas.create_text(200, 75, text= rand_name, fill="white", font=('Courier', 10))
    
    # Update text in Canvas 
    
    
    canvas.pack()
    
apps_menu.add_command(label="Random Location", command=lambda:my_w_child_randloc())



# Log menu
log_menu = Menu(
    menubar,
    tearoff=0
)

# Log menu items
log_menu.add_command(label='Power Time')
log_menu.add_command(label='Game Time')
log_menu.add_command(label='About')

# Log menu in menubar
menubar.add_cascade(
    label="Log",
    menu=log_menu,
    underline=0
)
# Config menu
config_menu = Menu(
    menubar,
    tearoff=0
)

# Config menu items
config_menu.add_command(label='Settings')
config_menu.add_command(label='About')

# Config menu in menubar
menubar.add_cascade(
    label="Config",
    menu=config_menu,
    underline=0
)


root.mainloop()
