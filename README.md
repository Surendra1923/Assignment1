# Assignment1

URL hashing system : 

functions and packages used in assignment.py 
 hashlib : this libraray will perfrom the hasing ot the given  url
 random : this package used for to generate random values( such as chars and digits )
 string :  string librarary used to generate string values 


FUNCTIONS:
generate_random_string():  it will return the a random end string

hash_url(url) : this function takes the url as param and it will do the hasing funtion and it return the url

shorten_url(original_url) :  this funtion takes the original url , from the user it will shorten the url with help of generate_random_sting() funtion 

resolve_url(token) :  this funtion will solve the shorten url, with reference to the token , and returns the orignal url 


STEPS:

1. takes url with utm :  original_url 
2. call shorten_url(original_url) : this funtion calls  the hash_url, generate_random_string() funtions to shorten the url and it will return the modified shorten url
3. resolved_url(token) :  to obtain the original url from the shorten url
