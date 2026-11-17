"""Candidate review of observed entry facts, never a completed transaction."""

def review_entries(entries):
    scenes = []
    for entry in entries:
        scene = entry['detail_fact']
        scenes.append({'scene_key': scene['business_key'], 'promotion': entry['catalog_fact']['condition'],
                       'detail_initial': scene['campaign'], 'signup_state': 'not_observed'})
    return scenes
