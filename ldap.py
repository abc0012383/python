from ldap3 import Server, Connection, ALL

server=Server('x.x.x.x',get_info=ALL)
conn=Connection(server,auto_bind=True,user='administrator@xxx.xxx',password='xxx',)
conn.search(search_base='ou=users,ou=China,ou=Corp,dc=xxx,dc=xxx',
            search_filter='(&(objectclass=person)(userAccountControl=512))',
            attributes=['pwdlastset','userPrincipalName','msDS-UserPasswordExpiryTimeComputed',],)
print(conn.entries)
