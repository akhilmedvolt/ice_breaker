import os, requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str = "None", mock: bool = False):
    if not mock:
        print("Using GIST")
        linkedin_profile_url = (
            "https://gist.githubusercontent.com/akhilmedvolt/52776969afccb8331a7749364f9a49cb/raw"
            "/0360cc5a1ac899db8f736fe6b0162bbede71b3b5/akhil-macro.json"
        )
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        print("Using PROXYCURL")
        return
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        params = {"url": linkedin_profile_url}
        headers = {"Authorization": "Bearer " + os.getenv("PROXYCURL_KEY")}
        response = requests.get(
            api_endpoint, params=params, headers=headers, timeout=10
        )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    return data


if __name__ == "__main__":
    linkedin_profile_url = "https://www.linkedin.com/in/akhilsanker/"
    scraped_data = scrape_linkedin_profile(linkedin_profile_url)
    print(scraped_data)
