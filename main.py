class Git:
  def __init__(self , username , useremail , rep_name) -> None:
    self.username= username
    self.useremail = useremail
    self.rep_name= rep_name

  def __repr__(self) -> str:
    return self.username +" "+ self.useremail
  


git_obj1 = Git('max' , 'max@gmail.com' , 'git')
git_obj2 = Git('ali' , 'ali@gmail.com' , 'calculator')


