import pusher
pusher_client = pusher.Pusher("320350", "949f0a6ddb5086f67ece", "7e54e76c710e7e734b8d")
print(pusher_client.notify(['lmao'],{
  'fcm': {
    'registration_id': ['eNg77zCaQLY:APA91bEZMATFgW8a-6-lqmsohU3tJ3kzLhol0NOJOG3h2e7c3mtSbgnYDJB9YaUVmdx-hIS_nI_OjbyCgYSzkXuHjnzOz2Ex-hkppaVSqQToHKVGwP-I5cVxvEpcGb3ILO3s_tZ2RlrQ'],    
    'notification': {
      'title': 'hello world',
      'body':'LMAOOOOOOOOO',
      'sound': 'default'
    }
  },
  'webhook_url': 'http://requestb.in/14oq16u1',
  'webhook_level': 'INFO'
}))
