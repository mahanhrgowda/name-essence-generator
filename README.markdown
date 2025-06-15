# Name Essence Generator

A Streamlit app that maps English phonemes to chakras, Bhavas, and Rasas, generating lore and images based on a name’s emotive essence using xAI’s Grok 2-1212 and Grok 2 Image Gen APIs.

## Repository Structure
- `streamlit/`: Files for Streamlit Community Cloud deployment.
- `render/`: Files for Render’s Dockerized deployment.

## Prerequisites
- **xAI API Key**: Obtain from [xAI API](https://x.ai/api) with 25 credits.
- **GitHub Account**: Public repository for deployment.
- **Google Colab Pro**: Optional for local testing.

## Deployment Instructions

### Streamlit Community Cloud
1. **Create Repository**:
   - Clone this repository:
     ```bash
     git clone https://github.com/your-username/name-essence-generator.git
     cd name-essence-generator
     ```

2. **Push to GitHub**:
   - Ensure `streamlit/app.py` and `streamlit/requirements.txt` are in the `streamlit` folder.
   - Commit and push:
     ```bash
     git add streamlit/*
     git commit -m "Add Streamlit deployment files"
     git push origin main
     ```

3. **Deploy**:
   - Sign up at [Streamlit Community Cloud](https://streamlit.io/cloud).
   - Click “Create app,” select the repository, and set:
     - Branch: `main`
     - Main file: `streamlit/app.py`
   - Add secret in “Advanced settings”:
     ```toml
     XAI_API_KEY = "your-xai-api-key"
     ```
   - Click “Deploy.” Access via the provided URL.

### Render Free Tier (Dockerized)
1. **Push to GitHub**:
   - Ensure `render/app.py`, `render/requirements.txt`, and `render/Dockerfile` are in the `render` folder.
   - Commit and push:
     ```bash
     git add render/*
     git commit -m "Add Render deployment files"
     git push origin main
     ```

2. **Deploy**:
   - Sign up at [Render](https://render.com).
   - Click “New” > “Web Service,” select the repository.
   - Configure:
     - Environment: Docker
     - Branch: `main`
     - Dockerfile Path: `render/Dockerfile`
     - Instance Type: Free (0.5 CPU, 512 MB RAM)
     - Environment Variable:
       - Key: `XAI_API_KEY`, Value: `your-xai-api-key`
   - Click “Create Web Service.” Access via the provided URL.

## Testing
- Enter a name (e.g., “Luna”).
- Expected output:
  - Phonemes: e.g., /ˈluːnə/
  - Chakra: e.g., Svadhisthana
  - Bhava: e.g., Hasya
  - Essence: e.g., Playful
  - Lore: 50-100 word story
  - Image: Vibrant scene

## Troubleshooting
- **API Errors**: Verify xAI API key and 25-credit limit.
- **Render Cold Starts**: Free tier may have delays.
- **Memory Issues**: Optimize dependencies if Render’s 512 MB RAM is exceeded.

## Resources
- [xAI API](https://x.ai/api)
- [Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud)
- [Render Deployment](https://render.com/docs)