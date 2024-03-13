# CAP-теорема
**Задача:** Объяснить согласно CAP-теореме к какой части можно отнести данные СУБД: DragonFly, Scylla, ArenaData
## DragonFly-CP
### Consistency(Согласованность):
  Согласованность заключается в поддержке репликации данных с первичного сервера на вторичный. То есть все вторичные сервера синхронизируются с главным сервером и в случае если первичный сервер становится не работоспособным то один ис вторичных серверов становится главным.
### Partition tolerance(Устойчивость к разделению системы):
  Заключается в том что DragonFly поддерживает архитектуру без разделения ресурсов(shared-nothing), подразумевающей, что к каждому потоку привязывается отдельный обособленный обработчик со своей порцией данных.
***Источник***: https://www.opennet.ru/opennews/art.shtml?num=58830


## Scylla-AP
### Non-Consistency(Несогласованность):
Фактор репликации (RF) эквивалентен количеству узлов, на которых данные (строки и разделы) реплицируются. Данные реплицируются на несколько (RF=N) узлов.

RF равный 1 означает, что в кластере есть только одна копия строки, и нет способа восстановить данные, если узел скомпрометирован или выходит из строя. RF=2 означает, что в кластере есть две копии строки. RF как минимум равный 3 используется в большинстве систем или аналогично. 


Уровень согласованности (CL) определяет, сколько реплик в кластере должны подтвердить операции чтения или записи перед тем, как они будут считаться успешными.

Т.е. все ноды не объязательно синхронизированы 

ScyllaDB выбирает доступность и устойчивость к разделению (partition tolerance) вместо согласованности.

### Availability(Доступность):
Если мы жертвуем согласованностью, мы можем обеспечить высокую доступность.

Во время сетевого разделения невозможно одновременно обеспечить как согласованность, так и высокую доступность.

### Partition tolerance(Устойчивость к разделению системы):
ScyllaDB запускает узлы в хеш-кольце. Все узлы равнозначны: здесь нет мастеров, слейвов или наборов реплик.
При оптимальном значения уровня согласованности и фактора репликации мы сможем при выхода из строя нескольких узлов все равно иметь достаточную работоспособность для того чтобы работало так же как перед выходом из строя этих нод так как у нас будут раскинуты копии данных из этих нод между остальными работаспособными узлами


***Источник***: Документация ScyllaDB - https://opensource.docs.scylladb.com/stable/architecture/architecture-fault-tolerance.html 



## ArenaData-CA
### Consistency(Согласованность):
  Arenadata DB построена на опенсорс системе Greenplum, и как и свой предшественник, соблюдает баланс между тремя характеристиками, заданными CAP-теоремой.
  Судя по данным из официального сайта, синхронизированность данных является большим приоритетом для данной СУБД.
### Availibality(доступность):
  Дальше, из заявления о соблюдении SLA, в которое входит время отклика, на уровне 99.8%, можно сделать вывод о высокой доступности системы
### Non-partition tolerance(неустойчивость к разделению)
  Умение продолжить работу при потере не более чем 50% узлов же говорит о достаточно высоком уровне устойчивости к разделению.
***Источник***:  https://arenadata.tech/products/arenadata-db/
                 https://docs.arenadata.io/ru/ADB/current/introduction/intro.html