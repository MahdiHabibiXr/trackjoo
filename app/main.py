import asyncio
from shazamio import Shazam

file_dir = 'files'
file_name = input('Enter the file name: ')
file = f'{file_dir}/{file_name}'

async def main():
    shazam = Shazam()
    out = await shazam.recognize_song(file)
    return out

out = asyncio.run(main())
print(out)
print('============================================')

# Extract track information
track = out['track']
title = track['title']
subtitle = track['subtitle']

# Extract image URLs
images = track['images']
coverart_hq_image = images['coverarthq']

# Extract other track details
url = track['url']

# Extract all links from hub and providers
print("\nAll Available Music Links:")

# Extract links from hub actions
if 'hub' in track and 'actions' in track['hub']:
    print("\nHub Actions:")
    for action in track['hub']['actions']:
        action_type = action.get('type', 'unknown')
        if 'uri' in action:
            print(f"{action_type}: {action['uri']}")
        elif 'id' in action:
            print(f"{action_type}: ID - {action['id']}")

def extract_hub_options(track):
    if 'hub' in track and 'options' in track['hub']:
        print("\nHub Options:")
        for option in track['hub']['options']:
            if 'actions' in option:
                for action in option['actions']:
                    action_name = action.get('name', 'unknown')
                    if 'uri' in action:
                        print(f"{action_name}: {action['uri']}")
                    elif 'id' in action:
                        print(f"{action_name}: ID - {action['id']}")

def extract_provider_links(track):
    if 'hub' in track and 'providers' in track['hub']:
        print("\nProvider Links:")
        for provider in track['hub']['providers']:
            provider_type = provider.get('type', 'unknown')
            provider_caption = provider.get('caption', provider_type)
            print(f"\n{provider_caption}:")
            
            if 'actions' in provider:
                for action in provider['actions']:
                    action_name = action.get('name', 'unknown')
                    if 'uri' in action:
                        print(f"- {action_name}: {action['uri']}")

def create_search_links(title, subtitle):
    if title and subtitle:
        search_query = f"{title} {subtitle}"
        encoded_query = search_query.replace(' ', '+')
        encoded_query_url = search_query.replace(' ', '%20')
        
        print("\nSearch Links:")
        print(f"YouTube Search: https://www.youtube.com/results?search_query={encoded_query}")
        print(f"SoundCloud Search: https://soundcloud.com/search?q={encoded_query_url}")
        print(f"Amazon Music Search: https://music.amazon.com/search/{encoded_query}")

# Call the functions
extract_hub_options(track)
extract_provider_links(track) 
create_search_links(title, subtitle)
