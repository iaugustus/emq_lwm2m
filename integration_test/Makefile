
.PHONY: clean, clean_result, start_broker  stop_broker  case1 case2 case3


EMQ    = emq-rel/relx.config
WAKAAMA  = build_wakaama/lightclient
PAHO_PYTHON = paho/mqtt/client.py

all:  clean_result $(EMQ) $(WAKAAMA) $(PAHO_PYTHON) start_broker clean_result case1 case2 case3 stop_broker
	@echo "  "
	@echo "  test complete"
	@echo "  "
	
clean_result:
	-rm -f case*.txt
	
start_broker:
	-rm -f emq-rel/_rel/emq/log/*
	-emq-rel/_rel/emq/bin/emq stop
	sleep 3
	emq-rel/_rel/emq/bin/emq start
	sleep 1
	emq-rel/_rel/emq/bin/emq_ctl plugins load emq_lwm2m


stop_broker:
	-emq-rel/_rel/emq/bin/emq stop
	

case1:
	-build_wakaama/lightclient -4 -n jXtestlwm2m &
	python case1.py
	-ps aux|grep lightclient|awk '{print $$2}'|xargs kill -2

case2:
	-build_wakaama/lightclient -4 -n jXtestlwm2m &
	python case2.py
	-ps aux|grep lightclient|awk '{print $$2}'|xargs kill -2

case3:
	-build_wakaama/lightclient -4 -n jXtestlwm2m &
	python case3.py
	-ps aux|grep lightclient|awk '{print $$2}'|xargs kill -2
	
	
$(EMQ):
	git clone https://github.com/emq/emq-rel.git
	git clone https://github.com/emq/emq-lwm2m.git
	@echo "update emq-lwm2m with this development code"
	mv emq-lwm2m  emq_lwm2m
	-rm -rf emq_lwm2m/etc
	-rm -rf emq_lwm2m/include
	-rm -rf emq_lwm2m/priv
	-rm -rf emq_lwm2m/src
	-rm -rf emq_lwm2m/Makefile
	-rm -rf emq_lwm2m/erlang.mk
	cp -rf ../etc       emq_lwm2m/
	cp -rf ../include   emq_lwm2m/
	cp -rf ../priv      emq_lwm2m/
	cp -rf ../src       emq_lwm2m/
	cp -rf ../Makefile  emq_lwm2m/Makefile
	cp -rf ../erlang.mk emq_lwm2m/erlang.mk
	-mkdir emq-rel/deps
	mv emq_lwm2m  emq-rel/deps/
	@echo "start building ..."
	python insert_lwm2m_plugin.py
	make -C emq-rel -f Makefile
	-cp -rf ../lwm2m_xml  emq-rel/_rel/emq/etc/


w:
	cd build_wakaama && cmake -DCMAKE_BUILD_TYPE=Debug ../wakaama/examples/lightclient && make

$(WAKAAMA):
	git clone https://github.com/eclipse/wakaama
	-mkdir build_wakaama
	cd build_wakaama && cmake -DCMAKE_BUILD_TYPE=Debug ../wakaama/examples/lightclient && make
	
	
mqtt: $(PAHO_PYTHON)
	# short for paho python client

$(PAHO_PYTHON):
	git clone https://github.com/eclipse/paho.mqtt.python.git
	mv paho.mqtt.python/src/paho ./
	rm -rf paho.mqtt.python
	
	
r: rebuild_emq
	# r short for rebuild_emq
	@echo " rebuild complete "
	
	
rebuild_emq:
	-emq-rel/_rel/emq/bin/emq stop
	-rm -rf emq-rel/deps/emq_lwm2m/etc
	-rm -rf emq-rel/deps/emq_lwm2m/include
	-rm -rf emq-rel/deps/emq_lwm2m/priv
	-rm -rf emq-rel/deps/emq_lwm2m/src
	-rm -rf emq-rel/deps/emq_lwm2m/Makefile
	-rm -rf emq-rel/deps/emq_lwm2m/erlang.mk
	cp -rf ../etc       emq-rel/deps/emq_lwm2m/
	cp -rf ../include   emq-rel/deps/emq_lwm2m/
	cp -rf ../priv      emq-rel/deps/emq_lwm2m/
	cp -rf ../src       emq-rel/deps/emq_lwm2m/
	cp -rf ../Makefile  emq-rel/deps/emq_lwm2m/Makefile
	cp -rf ../erlang.mk emq-rel/deps/emq_lwm2m/erlang.mk
	make -C emq-rel -f Makefile
	
	
clean: clean_result
	-rm -f client/*.exe
	-rm -f client/*.o
	-rm -rf emq-rel
	-rm -rf build_wakaama
	-rm -rf wakaama
	
	
	
lazy: clean_result start_broker case3 stop_broker
	# custom your command here
	@echo "you are so lazy"
	
	
	
