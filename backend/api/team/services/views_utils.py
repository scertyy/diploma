def get_team_and_user_data(request):
    data = request.data
    profile_id = data.get('profile_id')
    team_id = data.get('team_id')
    return profile_id, team_id
