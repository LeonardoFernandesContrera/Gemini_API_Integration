import google.generativeai as genai
import os 

GOOGLE_API_KEY = "YOUR API-KEY"

if not GOOGLE_API_KEY:
    raise ValueError("The Google_API_Key is not defined, please insert your API_Key before continue.")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')

try:
    with open("Mobile-Price-Prediction-cleaned_data.csv", "r") as f:
        computers_values = f.read()
        
    user_query_for_gemini = f"""
    Analyze the following dataset containing smartphone specifications and prices.
    Based on this data, provide an analysis of the key factors influencing smartphone prices.
    Furthermore, predict how the prices of *new* phones (considering trends in RAM, Storage, Camera, and Battery) might evolve in the near future.
    Suggest pricing strategies for hypothetical new phone models with advanced specifications.
    Please format your response using Markdown, including headings, bullet points, and tables where appropriate.

    Smartphone Data:
    {computers_values}
    """
    
    response = model.generate_content(user_query_for_gemini)
    
    gemini_output_text = response.text
    
    output_filename = "gemini_analysis_report.md"
    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.write("## Analysis by Google Gemini\n\n")
        outfile.write(gemini_output_text)
        print(f"\n--- Gemini's analysis saved to '{output_filename}' ---")
    
except Exception as e:
    print(f"\nSomething got wrong when communicating with Gemini API: {e}")
    print("Verify your API Key and your internet")
