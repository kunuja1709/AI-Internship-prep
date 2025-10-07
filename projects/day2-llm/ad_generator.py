"""
Location-Based Ad Copy Generator using Groq LLM
"""

import os
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ad_copy(business_type, location, target_audience):
    """Generate ad copy using LLM"""
    
    # Create prompt
    prompt = f"""
You are an expert advertising copywriter. Create 3 different ad copy variations for:

Business Type: {business_type}
Location: {location}
Target Audience: {target_audience}

Requirements:
- Each ad should be 50-70 words
- Include a strong call-to-action
- Mention the location naturally
- Make it engaging and persuasive
- Number each variation (1, 2, 3)

Format: Just provide the 3 ad copies, nothing else.
"""
    
    print("🔄 Generating ad copies using AI...")
    
    try:
        # Call Groq API
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        
        # Get response
        ad_copies = response.choices[0].message.content
        return ad_copies
        
    except Exception as e:
        return f"Error: {e}"


def main():
    print("\n" + "="*60)
    print("📢 LOCATION-BASED AD COPY GENERATOR")
    print("="*60)
    
    # Get user inputs
    business_type = input("\nBusiness type (e.g., Restaurant, Gym, Cafe): ")
    location = input("Location (e.g., Andheri Mumbai, MG Road Bangalore): ")
    target_audience = input("Target audience (e.g., Young professionals, Families): ")
    
    # Generate ad copies
    print("\n" + "="*60)
    result = generate_ad_copy(business_type, location, target_audience)
    print("\n✨ GENERATED AD COPIES:\n")
    print(result)
    print("\n" + "="*60)
    
    # Save to file
    filename = f"ads_{business_type.replace(' ', '_').lower()}.txt"
    with open(filename, 'w') as f:
        f.write(f"Business: {business_type}\n")
        f.write(f"Location: {location}\n")
        f.write(f"Audience: {target_audience}\n\n")
        f.write(result)
    
    print(f"\n💾 Saved to: {filename}")

if __name__ == "__main__":
    main()