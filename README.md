# 95888 DFP G2 Team 6 Final Project

### Team Members
Kaixin Tian     kaixint@andrew.cmu.edu  
Louie Sun       hongyuns@andrew.cmu.edu  
Yanting Hu      yantingh@andrew.cmu.edu  
Zheng Zhang     zhengzh2@andrew.cmu.edu   
Daochen Li      daochenl@andrew.cmu.edu  

### Application Information
CityPulse harnesses an extensive array of data, sourcing information from reputable platforms like Salary.com, WalletHub.com, Numbeo.com, and others.
The pivotal metrics encompass a spectrum of factors, including 1.Average Household Income, 2.Employment Rate, 3.Cost of Living Percentage, 4.Safety Index, 5.Health Care Exp Index, 6.Pollution Index, and 7.Recreation Total Score.
These metrics, carefully weighted and curated, empower users to navigate relocation decisions with a wealth of informed insights.
By regularly refreshing the data utilized within the application, CityPulse remains dynamic and aligned with the latest trends and conditions, offering users a consistently reliable tool for making well-informed decisions about their prospective relocations.

### Relocation Recommendation Metrics:  
1. Income: Average Household Income
2. Employment: Employment Rate
3. Cost: Cost of Living Percentage
4. Safety: Safety Index
5. Medical: Health Care Exp Index
6. Pollution: Pollution Index
7. Recreation: Recreation Total Score

### Sources
1. Average Household Income: https://data.census.gov
2. Employment Rate: https://data.census.gov
3. Cost of Living Percentage: https://www.salary.com/research/cost-of-living/
4. Safety Index: https://www.numbeo.com/crime/rankings_current.jsp
5. Health Exp Index: https://www.numbeo.com/health-care/rankings_current.jsp
6. Pollution Index: https://www.numbeo.com/pollution/rankings_current.jsp
7. Recreation Total Score: https://wallethub.com/edu/best-worst-cities-for-recreation/5144

### Steps To Install & Run
1. Download the entire zip package (say on Desktop) and unzip the package;
2. Go to the directory named CityPulse with main application named CityPulse.py (For example, if you put the entire package on Desktop, use "cd /Users/username/Desktop/CityPulse" to go to the directory);
3. Run the application using terminal: "python3 CityPulse.py", (this main program file imports other modules/code files that accomplish various parts of the overall application);
4. Or run "CityPulse.py" using IDEs such as PyCharm or Spyder.

### Additional Setup Information
1. No additional module needed;
2. API key for Census.gov in average_household_income.py and employment_rate.py are hardcoded into the .py files, no need to obtain further;
3. cost_of_living.py might take a few longer than other crawlers, but within minutes;
4. IP may be banned running recreation.py for many times, try using VPN or Hotspot;
5. Fresh data is included in ./data directory, run ./gui/ui.py to skip the download.

Please see setup.mp4 for more details.