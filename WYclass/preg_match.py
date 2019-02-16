def numUniqueEmails(emails):
    emailsLen = len(emails)
    newEmails = []
    if not emailsLen > 100 and emailsLen > 0:
        for i in emails:
            if not len(i) > 100 and len(i) > 0:
                subEmail = ""
                email = i.split('@')
                if email[1].count('.') == 1:
                    subE = email[0].split('+')
                    subNoPoint = subE[0].split('.')
                    for j in subNoPoint:
                        subEmail = subEmail + j
                    newEmail = subEmail + "@" + email[1]
                    newEmails.append(newEmail)
    print(len(newEmails))
    return len(newEmails)


emails = ["fg.r.u.uzj+o.pw@kziczvh.com", "r.cyo.g+d.h+b.ja@tgsg.z.com", "fg.r.u.uzj+o.f.d@kziczvh.com",
          "r.cyo.g+ng.r.iq@tgsg.z.com", "fg.r.u.uzj+lp.k@kziczvh.com", "r.cyo.g+n.h.e+n.g@tgsg.z.com",
          "fg.r.u.uzj+k+p.j@kziczvh.com", "fg.r.u.uzj+w.y+b@kziczvh.com", "r.cyo.g+x+d.c+f.t@tgsg.z.com",
          "r.cyo.g+x+t.y.l.i@tgsg.z.com", "r.cyo.g+brxxi@tgsg.z.com", "r.cyo.g+z+dr.k.u@tgsg.z.com",
          "r.cyo.g+d+l.c.n+g@tgsg.z.com", "fg.r.u.uzj+vq.o@kziczvh.com", "fg.r.u.uzj+uzq@kziczvh.com",
          "fg.r.u.uzj+mvz@kziczvh.com", "fg.r.u.uzj+taj@kziczvh.com", "fg.r.u.uzj+fek@kziczvh.com"]
numUniqueEmails(emails)
