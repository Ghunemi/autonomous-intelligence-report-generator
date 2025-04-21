+-------------+                          
|  User/CLI   |                          
+-------------+                          
      |                                   
      v                                   
+----------------+                        
| run_pipeline() |                        
+----------------+                        
      |                                   
      v                                   
+--------------------------------+       
| 1) Web Search & Scrape         |       
|   • DuckDuckGo API             |       
|   • requests + BeautifulSoup   |       
+--------------------------------+       
      |                                   
      v                                   
+----------------------+                
| sources: list of     |                
| {url, snippet, text} |                
+----------------------+                
      |                                   
      v                                   
+--------------------------------+       
| 2) Insight Extraction           |       
|   • LLMChain prompts           |       
|   • ChatOllama @ localhost     |       
+--------------------------------+       
      |                                   
      v                                   
+-----------------------------+           
| insights: {                  |          
|   trends, competitors+notes, |          
|   recommendations }          |          
+-----------------------------+           
      |                                   
      v                                   
+-----------------------------+           
| 3) Report Writer             |          
|   • python‑docx              |          
|   • Jinja‑style templating   |          
+-----------------------------+           
      |                                   
      v                                   
+-----------------------------+           
| output/*.docx                |          
| (Trends, Competitor Table,   |          
|  Recommendations, Sources)   |          
+-----------------------------+           
