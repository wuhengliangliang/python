backend www.oldboy1.org
        server 101.1000.7.9 101.1000.7.9 weight 20 maxconn 30
        server 10.1000.7.9 100.1000.7.9 weight 2 maxconn 30
        server 100.10.7.9 100.1000.7.9 weight 20 maxconn 30
        server 2.2.2.4 2.2.2.4 weight 20 maxconn 3000
backend www.oldboy2.org
        server 100.1000.7.9 100.1000.7.9 weight 20 maxconn 30
        server 10.1000.7.9 100.1000.7.9 weight 2 maxconn 30
        server 100.10.7.9 100.1000.7.9 weight 20 maxconn 30
        server 100.1000.7.9 10.100.7.9 weight 20 maxconn 30
backend www.oldboy3.org
        server 100.1000.7.9 100.1000.7.9 weight 20 maxconn 30
        server 10.1000.7.9 100.1000.7.9 weight 2 maxconn 30
        server 100.10.7.9 100.1000.7.9 weight 20 maxconn 30
        server 100.1000.7.9 10.100.7.9 weight 20 maxconn 30