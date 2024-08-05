import requests

def obtener_plantas(api_key, url):
    params = {
        'token': api_key,
        'limit': 100
    }
    
    ids_vistas = set()
    plantas = []

    page = 1
    while True:
        params['page'] = page
        response = requests.get(url, params=params)
        data = response.json()
        
        if not data.get('data'):
            break
        
        for planta in data['data']:
            planta_id = planta.get('id')
            cuidados = planta.get('care_instructions', 'No disponible')
            
            if planta_id not in ids_vistas:
                ids_vistas.add(planta_id)
                plantas.append((planta_id, cuidados))
        
        page += 1
    
    return plantas