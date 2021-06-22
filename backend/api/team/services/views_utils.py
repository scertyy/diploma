def get_team_and_user_data(request):
    data = request.data
    contributor_id = data.get('contributor_id')
    team_id = data.get('team_id')
    return contributor_id, team_id
