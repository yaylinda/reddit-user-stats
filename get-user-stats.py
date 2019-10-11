import praw
import argparse
import csv

def export_data_to_csv(data):
  filename = 'data.csv'
  column_names = list(data[0].keys())

  print('[log] writing data to csv, filename=%s' % filename)

  csv_file = open(filename, 'w')
  csv_writer = csv.writer(csv_file, delimiter=',')
  csv_writer.writerow(column_names)
  
  for datum in data:
    csv_writer.writerow([datum[column_names[x]] for x in range(0, len(column_names))])

  csv_file.close()

  print('[log] completed writing csv')

def get_data(redditor):

  data = []
  num_submissions = 0
  num_comments = 0

  print('[log] collecting submissions')

  for submission in redditor.submissions.new(limit = None):
    datum = {}
    datum['score'] = submission.score
    datum['created_utc'] = submission.created_utc
    datum['subreddit'] = submission.subreddit.display_name
    datum['type'] = "Submission"
    data.append(datum)
    num_submissions = num_submissions + 1

  print('[log] collected %d submissions' % num_submissions)

  print('[log] collecting comments')

  for comment in redditor.comments.new(limit = None):
    datum = {}
    datum["score"] = comment.score
    datum["created_utc"] = comment.created_utc
    datum["subreddit"] = comment.subreddit.display_name
    datum["type"] = "Comment"
    data.append(datum)
    num_comments = num_comments + 1

  print('[log] collected %d comments' % num_comments)

  return data


"""
"""
def main():
  parser = argparse.ArgumentParser(description = 'Get Reddit user stats')
  parser.add_argument('--username', type = str, help = 'Reddit username')
  args = parser.parse_args()

  redditor = praw.Reddit('default').redditor(args.username)

  data = get_data(redditor)

  export_data_to_csv(data)


if __name__ == '__main__':
  main()