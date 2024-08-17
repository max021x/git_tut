import uuid
class Git:
  def __init__(self , username , useremail , rep_name) -> None:
    self.username= username
    self.useremail = useremail
    self.rep_name= rep_name
    self.id = uuid.uuid4()
  def __repr__(self) -> str:
    return self.username +" ==> "+ self.useremail
  
  
  def __hash__(self) -> int:
    return hash(self.id)


class Company():
  def __init__(self , size) -> None:
    self.size = size
    self.repos = []

  def __add__(self, other):
    if not isinstance(other , Git):
      raise TypeError('Not a Git repo ..')
    self.repos.append(other)
    return self
  
  def __iter__(self):
    return iter(self.repos)



class NoUpdateDictionary(dict):
  def __setitem__(self, key, value) -> None:
    if key in self:
      raise KeyError('key allreay exist ..')
    super().__setitem__(key  , value)



dic = NoUpdateDictionary()
dic['test'] = 12
dic['test'] = 20
